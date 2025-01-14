#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : pypi-poetry
Version  : 2.0.1
Release  : 57
URL      : https://files.pythonhosted.org/packages/3c/8b/5467e3301050055d365e602cc6ba574ee4fbc8163aeec213e5a75b3f219b/poetry-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3c/8b/5467e3301050055d365e602cc6ba574ee4fbc8163aeec213e5a75b3f219b/poetry-2.0.1.tar.gz
Summary  : Python dependency management and packaging made easy.
Group    : Development/Tools
License  : MIT
Requires: pypi-poetry-bin = %{version}-%{release}
Requires: pypi-poetry-license = %{version}-%{release}
Requires: pypi-poetry-python = %{version}-%{release}
Requires: pypi-poetry-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Poetry: Python packaging and dependency management made easy
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Stable Version](https://img.shields.io/pypi/v/poetry?label=stable)][PyPI Releases]
[![Pre-release Version](https://img.shields.io/github/v/release/python-poetry/poetry?label=pre-release&include_prereleases&sort=semver)][PyPI Releases]
[![Python Versions](https://img.shields.io/pypi/pyversions/poetry)][PyPI]
[![Download Stats](https://img.shields.io/pypi/dm/poetry)](https://pypistats.org/packages/poetry)
[![Discord](https://img.shields.io/discord/487711540787675139?logo=discord)][Discord]

%package bin
Summary: bin components for the pypi-poetry package.
Group: Binaries
Requires: pypi-poetry-license = %{version}-%{release}

%description bin
bin components for the pypi-poetry package.


%package license
Summary: license components for the pypi-poetry package.
Group: Default

%description license
license components for the pypi-poetry package.


%package python
Summary: python components for the pypi-poetry package.
Group: Default
Requires: pypi-poetry-python3 = %{version}-%{release}

%description python
python components for the pypi-poetry package.


%package python3
Summary: python3 components for the pypi-poetry package.
Group: Default
Requires: python3-core
Provides: pypi(poetry)
Requires: pypi(build)
Requires: pypi(cachecontrol)
Requires: pypi(cleo)
Requires: pypi(dulwich)
Requires: pypi(fastjsonschema)
Requires: pypi(installer)
Requires: pypi(keyring)
Requires: pypi(packaging)
Requires: pypi(pkginfo)
Requires: pypi(platformdirs)
Requires: pypi(poetry_core)
Requires: pypi(pyproject_hooks)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)
Requires: pypi(shellingham)
Requires: pypi(tomlkit)
Requires: pypi(trove_classifiers)
Requires: pypi(virtualenv)
Requires: pypi-html5lib
Provides: pypi(poetry)

%description python3
python3 components for the pypi-poetry package.


%prep
%setup -q -n poetry-2.0.1
cd %{_builddir}/poetry-2.0.1
pushd ..
cp -a poetry-2.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736875919
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . crashtest
pypi-dep-fix.py . keyring
pypi-dep-fix.py . packaging
pypi-dep-fix.py . poetry-core
pypi-dep-fix.py . requests-toolbelt
pypi-dep-fix.py . cleo
pypi-dep-fix.py . platformdirs
pypi-dep-fix.py . installer
pypi-dep-fix.py . trove-classifiers
pypi-dep-fix.py . cachecontrol
pypi-dep-fix.py . build
pypi-dep-fix.py . jsonschema
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . crashtest
pypi-dep-fix.py . keyring
pypi-dep-fix.py . packaging
pypi-dep-fix.py . poetry-core
pypi-dep-fix.py . requests-toolbelt
pypi-dep-fix.py . cleo
pypi-dep-fix.py . platformdirs
pypi-dep-fix.py . installer
pypi-dep-fix.py . trove-classifiers
pypi-dep-fix.py . cachecontrol
pypi-dep-fix.py . build
pypi-dep-fix.py . jsonschema
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-poetry
cp %{_builddir}/poetry-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry/7bc236a823ce6ebdaa7c2490792581b9ed00afe7 || :
cp %{_builddir}/poetry-%{version}/tests/fixtures/with-include/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry/84661790a5df00ab944c2d37978d6ce5ac88e554 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} crashtest
pypi-dep-fix.py %{buildroot} keyring
pypi-dep-fix.py %{buildroot} packaging
pypi-dep-fix.py %{buildroot} poetry-core
pypi-dep-fix.py %{buildroot} requests-toolbelt
pypi-dep-fix.py %{buildroot} cleo
pypi-dep-fix.py %{buildroot} platformdirs
pypi-dep-fix.py %{buildroot} installer
pypi-dep-fix.py %{buildroot} trove-classifiers
pypi-dep-fix.py %{buildroot} cachecontrol
pypi-dep-fix.py %{buildroot} build
pypi-dep-fix.py %{buildroot} jsonschema
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/poetry/__init__.py
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/poetry/__pycache__/__init__.cpython-3*.pyc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/poetry

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-poetry/7bc236a823ce6ebdaa7c2490792581b9ed00afe7
/usr/share/package-licenses/pypi-poetry/84661790a5df00ab944c2d37978d6ce5ac88e554

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
