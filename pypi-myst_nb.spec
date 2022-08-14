#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-myst_nb
Version  : 0.16.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/44/31/5c56a1d918d3d0c8f7af9129a446171ae0c7a59097fa6db707d389b3dd73/myst-nb-0.16.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/44/31/5c56a1d918d3d0c8f7af9129a446171ae0c7a59097fa6db707d389b3dd73/myst-nb-0.16.0.tar.gz
Summary  : A Jupyter Notebook Sphinx reader built on top of the MyST markdown parser.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-myst_nb-bin = %{version}-%{release}
Requires: pypi-myst_nb-license = %{version}-%{release}
Requires: pypi-myst_nb-python = %{version}-%{release}
Requires: pypi-myst_nb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# MyST-NB
[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![PyPI][pypi-badge]][pypi-link]
[![Conda Version][conda-badge]][conda-link]

%package bin
Summary: bin components for the pypi-myst_nb package.
Group: Binaries
Requires: pypi-myst_nb-license = %{version}-%{release}

%description bin
bin components for the pypi-myst_nb package.


%package license
Summary: license components for the pypi-myst_nb package.
Group: Default

%description license
license components for the pypi-myst_nb package.


%package python
Summary: python components for the pypi-myst_nb package.
Group: Default
Requires: pypi-myst_nb-python3 = %{version}-%{release}

%description python
python components for the pypi-myst_nb package.


%package python3
Summary: python3 components for the pypi-myst_nb package.
Group: Default
Requires: python3-core
Provides: pypi(myst_nb)
Requires: pypi(importlib_metadata)
Requires: pypi(ipykernel)
Requires: pypi(ipython)
Requires: pypi(jupyter_cache)
Requires: pypi(myst_parser)
Requires: pypi(nbclient)
Requires: pypi(nbformat)
Requires: pypi(pyyaml)
Requires: pypi(sphinx)
Requires: pypi(sphinx_togglebutton)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-myst_nb package.


%prep
%setup -q -n myst-nb-0.16.0
cd %{_builddir}/myst-nb-0.16.0
pushd ..
cp -a myst-nb-0.16.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658957133
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-myst_nb
cp %{_builddir}/myst-nb-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-myst_nb/f6901900cf039247901977f1db5534db7b54141b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mystnb-docutils-html
/usr/bin/mystnb-docutils-html5
/usr/bin/mystnb-docutils-latex
/usr/bin/mystnb-docutils-pseudoxml
/usr/bin/mystnb-docutils-xml
/usr/bin/mystnb-quickstart
/usr/bin/mystnb-to-jupyter

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-myst_nb/f6901900cf039247901977f1db5534db7b54141b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
