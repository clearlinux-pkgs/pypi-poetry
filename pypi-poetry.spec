#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-poetry
Version  : 1.1.15
Release  : 18
URL      : https://files.pythonhosted.org/packages/e0/c8/09e126761651e291ab54db1b1d6983c64a1cf67b8b25ce9c806db23e16ab/poetry-1.1.15.tar.gz
Source0  : https://files.pythonhosted.org/packages/e0/c8/09e126761651e291ab54db1b1d6983c64a1cf67b8b25ce9c806db23e16ab/poetry-1.1.15.tar.gz
Summary  : Python dependency management and packaging made easy.
Group    : Development/Tools
License  : MIT
Requires: pypi-poetry-bin = %{version}-%{release}
Requires: pypi-poetry-license = %{version}-%{release}
Requires: pypi-poetry-python = %{version}-%{release}
Requires: pypi-poetry-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
# Poetry: Dependency Management for Python
Poetry helps you declare, manage and install dependencies of Python projects,
ensuring you have the right stack everywhere.

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
Requires: pypi(cachecontrol)
Requires: pypi(cachy)
Requires: pypi(cleo)
Requires: pypi(clikit)
Requires: pypi(crashtest)
Requires: pypi(html5lib)
Requires: pypi(keyring)
Requires: pypi(packaging)
Requires: pypi(pexpect)
Requires: pypi(pkginfo)
Requires: pypi(poetry_core)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)
Requires: pypi(shellingham)
Requires: pypi(tomlkit)
Requires: pypi(virtualenv)

%description python3
python3 components for the pypi-poetry package.


%prep
%setup -q -n poetry-1.1.15
cd %{_builddir}/poetry-1.1.15
pushd ..
cp -a poetry-1.1.15 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661193433
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . crashtest
pypi-dep-fix.py . keyring
pypi-dep-fix.py . packaging
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . crashtest
pypi-dep-fix.py . keyring
pypi-dep-fix.py . packaging
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-poetry
cp %{_builddir}/poetry-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry/84661790a5df00ab944c2d37978d6ce5ac88e554
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} crashtest
pypi-dep-fix.py %{buildroot} keyring
pypi-dep-fix.py %{buildroot} packaging
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
/usr/share/package-licenses/pypi-poetry/84661790a5df00ab944c2d37978d6ce5ac88e554

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
