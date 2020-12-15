#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyOpenGL
Version  : 3.1.5
Release  : 15
URL      : https://files.pythonhosted.org/packages/b8/73/31c8177f3d236e9a5424f7267659c70ccea604dab0585bfcd55828397746/PyOpenGL-3.1.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/b8/73/31c8177f3d236e9a5424f7267659c70ccea604dab0585bfcd55828397746/PyOpenGL-3.1.5.tar.gz
Summary  : Standard OpenGL bindings for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: PyOpenGL-license = %{version}-%{release}
Requires: PyOpenGL-python = %{version}-%{release}
Requires: PyOpenGL-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=================================

%package license
Summary: license components for the PyOpenGL package.
Group: Default

%description license
license components for the PyOpenGL package.


%package python
Summary: python components for the PyOpenGL package.
Group: Default
Requires: PyOpenGL-python3 = %{version}-%{release}
Provides: pyopengl-python

%description python
python components for the PyOpenGL package.


%package python3
Summary: python3 components for the PyOpenGL package.
Group: Default
Requires: python3-core
Provides: pypi(pyopengl)

%description python3
python3 components for the PyOpenGL package.


%prep
%setup -q -n PyOpenGL-3.1.5
cd %{_builddir}/PyOpenGL-3.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603400858
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PyOpenGL
cp %{_builddir}/PyOpenGL-3.1.5/license.txt %{buildroot}/usr/share/package-licenses/PyOpenGL/f6479ca0a457064e71273860ec9eb1fd2423298e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyOpenGL/f6479ca0a457064e71273860ec9eb1fd2423298e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
