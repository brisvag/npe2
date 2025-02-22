import json

import pytest
from pydantic import ValidationError

from npe2 import PluginManifest
from npe2.manifest import _validators

# the docstrings here are used to assert the validation error that is printed.

SAMPLE_PLUGIN_NAME = "my-plugin"


def _mutator_invalid_package_name(data):
    """'invalid??' is not a valid python package name."""
    data["name"] = "invalid??"


def _mutator_invalid_package_name2(data):
    """'_invalid' is not a valid python package name."""
    data["name"] = "_invalid"


def _mutator_command_not_begin_with_package_name(data):
    """Commands identifiers must start with the current package name"""
    assert "contributions" in data
    c = data["contributions"]["commands"][0]["id"]
    data["contributions"]["commands"][0]["id"] = ".".join(
        ["not_packagename", *c.split(".")[1:]]
    )


def _mutator_python_name_no_colon(data):
    """'this.has.no.colon' is not a valid python_name."""
    assert "contributions" in data
    data["contributions"]["commands"][0]["python_name"] = "this.has.no.colon"


def _mutator_python_name_starts_with_number(data):
    """'1starts_with_number' is not a valid python_name."""
    assert "contributions" in data
    data["contributions"]["commands"][0]["python_name"] = "1starts_with_number"


def _mutator_no_contributes_extra_field(data):
    """extra fields not permitted"""
    # Contributions used to be called contributes.
    data["invalid_extra_name"] = data["contributions"]
    del data["contributions"]


def _mutator_writer_requires_non_empty_layer_types(data):
    """layer_types must not be empty"""
    data["contributions"]["writers"][0]["layer_types"] = []


def _mutator_writer_invalid_layer_type_constraint(data):
    """'image{' is not a valid LayerType"""
    data["contributions"]["writers"][0]["layer_types"].append("image{")


def _mutator_writer_invalid_file_extension_1(data):
    """Invalid file extension: Must have one character past the '.'"""
    data["contributions"]["writers"][0]["filename_extensions"] = ["*"]


def _mutator_writer_invalid_file_extension_2(data):
    """Invalid file extension: Must have one character past the '.'"""
    data["contributions"]["writers"][0]["filename_extensions"] = ["."]


def _mutator_schema_version_too_high(data):
    """The declared schema version '999.999.999' is newer than npe2's schema version"""
    data["schema_version"] = "999.999.999"


@pytest.mark.parametrize(
    "mutator",
    [
        _mutator_invalid_package_name,
        _mutator_invalid_package_name2,
        _mutator_command_not_begin_with_package_name,
        _mutator_python_name_no_colon,
        _mutator_python_name_starts_with_number,
        _mutator_no_contributes_extra_field,
        _mutator_writer_requires_non_empty_layer_types,
        _mutator_writer_invalid_layer_type_constraint,
        _mutator_writer_invalid_file_extension_1,
        _mutator_writer_invalid_file_extension_2,
        _mutator_schema_version_too_high,
    ],
)
def test_invalid(mutator, uses_sample_plugin):
    result = next(
        result
        for result in PluginManifest.discover()
        if result.manifest and result.manifest.name == SAMPLE_PLUGIN_NAME
    )
    assert result.error is None
    assert result.manifest is not None
    pm = result.manifest
    data = json.loads(pm.json(exclude_unset=True))
    mutator(data)
    with pytest.raises(ValidationError) as excinfo:
        PluginManifest(**data)
    assert mutator.__doc__ in str(excinfo.value)


def test_invalid_python_name(uses_sample_plugin):
    mf = next(
        result
        for result in PluginManifest.discover()
        if result.manifest and result.manifest.name == SAMPLE_PLUGIN_NAME
    ).manifest
    assert mf and mf.contributions and mf.contributions.commands
    assert mf.contributions.commands[-1].python_name

    assert mf.validate_imports() is None
    mf.contributions.commands[-1].python_name += "_whoops"  # type: ignore
    with pytest.raises(ValidationError) as e:
        mf.validate_imports()
    assert "has no attribute 'make_widget_from_function_whoops'" in str(e.value)


def _valid_mutator_no_contributions(data):
    """
    Contributions can be absent, in which case the Pydantic model will set the
    default value to None, and not the empty list, make sure that works.
    """
    del data["contributions"]


def _valid_mutator_no_contributions_None(data):
    """
    Contributions can be absent, in which case the Pydantic model will set the
    default value to None, and not the empty list, make sure that works.
    """
    data["contributions"] = None


@pytest.mark.parametrize(
    "mutator",
    [_valid_mutator_no_contributions, _valid_mutator_no_contributions_None],
)
def test_valid_mutations(mutator, uses_sample_plugin):
    assert mutator.__name__.startswith("_valid")

    pm = list(PluginManifest.discover())[0]
    assert pm.manifest
    # make sure the data is a copy as we'll mutate it
    data = json.loads(pm.manifest.json(exclude_unset=True))
    mutator(data)
    PluginManifest(**data)


@pytest.mark.parametrize(
    "display_name",
    [
        "Here there everywhere and more with giggles and friends",
        "ab",
        " abc",
        "abc ",
        "_abc",
        "abc_",
        "abc♱",
    ],
)
def test_invalid_display_names(display_name, uses_sample_plugin):
    field = PluginManifest.__fields__["display_name"]
    value, err = field.validate(display_name, {}, loc="display_name")
    assert err is not None


@pytest.mark.parametrize(
    "display_name",
    [
        "Some Cell & Stru买cture Segmenter",
        "Segment Blobs and Things with Membranes",
        "abc",
        "abc䜁䜂",
    ],
)
def test_valid_display_names(display_name, uses_sample_plugin):
    field = PluginManifest.__fields__["display_name"]
    value, err = field.validate(display_name, {}, loc="display_name")
    assert err is None


def test_display_name_default_is_valid():
    PluginManifest(name="")


@pytest.mark.parametrize(
    "expr",
    [
        "vectors{",
        "image",  # should parse fine, but be a duplication error
        "vectors{8,3}",
        "vectors{-1}",
        "vectors??",
        "other?",
    ],
)
def test_writer_invalid_layer_type_expressions(expr, uses_sample_plugin):
    result = next(
        result
        for result in PluginManifest.discover()
        if result.manifest and result.manifest.name == SAMPLE_PLUGIN_NAME
    )
    assert result.error is None
    assert result.manifest is not None
    pm = result.manifest
    data = json.loads(pm.json(exclude_unset=True))

    assert "contributions" in data
    assert "writers" in data["contributions"]
    data["contributions"]["writers"][0]["layer_types"].append(expr)

    with pytest.raises(ValidationError):
        PluginManifest(**data)


@pytest.mark.parametrize("id", ["badchar!?", "-bad-start", "has space"])
def test_invalid_command_id(id):
    with pytest.raises(ValueError):
        _validators.command_id(id)
