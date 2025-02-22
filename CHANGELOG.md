# Changelog

## [v0.1.0](https://github.com/napari/npe2/tree/v0.1.0) (2021-12-15)

[Full Changelog](https://github.com/napari/npe2/compare/v0.1.0rc1...v0.1.0)

**Implemented enhancements:**

- Remove semver dependency, vendor small portion [\#62](https://github.com/napari/npe2/pull/62) ([tlambert03](https://github.com/tlambert03))
- Make `npe2 convert` modify a repository [\#60](https://github.com/napari/npe2/pull/60) ([tlambert03](https://github.com/tlambert03))
- Delay import of `cmd.python_name` until needed [\#55](https://github.com/napari/npe2/pull/55) ([tlambert03](https://github.com/tlambert03))
- Add autogenerate\_from\_command field to Widget contribution [\#51](https://github.com/napari/npe2/pull/51) ([tlambert03](https://github.com/tlambert03))
- Update error messages [\#46](https://github.com/napari/npe2/pull/46) ([ppwadhwa](https://github.com/ppwadhwa))
- PackageMetadata field [\#44](https://github.com/napari/npe2/pull/44) ([tlambert03](https://github.com/tlambert03))

**Tests & CI:**

- add changelog generator config [\#65](https://github.com/napari/npe2/pull/65) ([tlambert03](https://github.com/tlambert03))
- Test conversion for all plugins [\#52](https://github.com/napari/npe2/pull/52) ([tlambert03](https://github.com/tlambert03))

**Refactors:**

- Start to make command APIs clearer [\#61](https://github.com/napari/npe2/pull/61) ([tlambert03](https://github.com/tlambert03))
- rename autogenerate field \(\#53\) [\#58](https://github.com/napari/npe2/pull/58) ([nclack](https://github.com/nclack))
- Schema review [\#49](https://github.com/napari/npe2/pull/49) ([nclack](https://github.com/nclack))

## [v0.1.0rc1](https://github.com/napari/npe2/tree/v0.1.0rc1) (2021-12-03)

[Full Changelog](https://github.com/napari/npe2/compare/v0.0.1rc1...v0.1.0rc1)

**Implemented enhancements:**

- add `get_callable` to Executable mixin [\#34](https://github.com/napari/npe2/pull/34) ([tlambert03](https://github.com/tlambert03))
- Sample data [\#31](https://github.com/napari/npe2/pull/31) ([tlambert03](https://github.com/tlambert03))
- support for Dock Widgets [\#26](https://github.com/napari/npe2/pull/26) ([tlambert03](https://github.com/tlambert03))
- Manifest cli [\#20](https://github.com/napari/npe2/pull/20) ([ppwadhwa](https://github.com/ppwadhwa))

**Tests & CI:**

- use pytomlpp, and test toml/json round trips [\#43](https://github.com/napari/npe2/pull/43) ([tlambert03](https://github.com/tlambert03))
- prep for release [\#42](https://github.com/napari/npe2/pull/42) ([tlambert03](https://github.com/tlambert03))

**Refactors:**

- Change 'publisher' to 'author' \(\#39\) [\#40](https://github.com/napari/npe2/pull/40) ([nclack](https://github.com/nclack))
- Cleanup manifest [\#38](https://github.com/napari/npe2/pull/38) ([nclack](https://github.com/nclack))

## [v0.0.1rc1](https://github.com/napari/npe2/tree/v0.0.1rc1) (2021-11-17)

[Full Changelog](https://github.com/napari/npe2/compare/cdbe96c3f0ea8c0e3ad050e91c24b40029cc0387...v0.0.1rc1)

**Implemented enhancements:**

- Small updates for napari [\#25](https://github.com/napari/npe2/pull/25) ([tlambert03](https://github.com/tlambert03))
- Add display\_name validation [\#23](https://github.com/napari/npe2/pull/23) ([nclack](https://github.com/nclack))
- Prevent extra fields in Commands. [\#15](https://github.com/napari/npe2/pull/15) ([Carreau](https://github.com/Carreau))
- More Validation. [\#14](https://github.com/napari/npe2/pull/14) ([Carreau](https://github.com/Carreau))
- Add debug to help diagnosing non-validation errors. [\#12](https://github.com/napari/npe2/pull/12) ([Carreau](https://github.com/Carreau))
- Add support for writer plugins [\#3](https://github.com/napari/npe2/pull/3) ([nclack](https://github.com/nclack))
- Some extra validation and allow to execute module with -m [\#1](https://github.com/napari/npe2/pull/1) ([Carreau](https://github.com/Carreau))

**Tests & CI:**

- Better pytest error on invalid schema. [\#11](https://github.com/napari/npe2/pull/11) ([Carreau](https://github.com/Carreau))
- Misc validation and testing. [\#5](https://github.com/napari/npe2/pull/5) ([Carreau](https://github.com/Carreau))
- Implement linting, CI, add basic tests [\#4](https://github.com/napari/npe2/pull/4) ([tlambert03](https://github.com/tlambert03))

**Refactors:**

- General refactor, Exectuable mixin, io\_utils APIs, remove some globals [\#18](https://github.com/napari/npe2/pull/18) ([tlambert03](https://github.com/tlambert03))
- Rename command command field to id. [\#10](https://github.com/napari/npe2/pull/10) ([Carreau](https://github.com/Carreau))
- Rename contributes to contributions ? [\#8](https://github.com/napari/npe2/pull/8) ([Carreau](https://github.com/Carreau))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
