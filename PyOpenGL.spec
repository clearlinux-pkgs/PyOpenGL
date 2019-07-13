#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x65BB76AA6EB7E943 (mcfletch@vrplumber.com)
#
Name     : PyOpenGL
Version  : 3.1.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/9c/1d/4544708aaa89f26c97cc09450bb333a23724a320923e74d73e028b3560f9/PyOpenGL-3.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/9c/1d/4544708aaa89f26c97cc09450bb333a23724a320923e74d73e028b3560f9/PyOpenGL-3.1.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/9c/1d/4544708aaa89f26c97cc09450bb333a23724a320923e74d73e028b3560f9/PyOpenGL-3.1.0.tar.gz.asc
Summary  : Standard OpenGL bindings for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: PyOpenGL-license = %{version}-%{release}
Requires: PyOpenGL-python = %{version}-%{release}
Requires: PyOpenGL-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

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

%description python3
python3 components for the PyOpenGL package.


%prep
%setup -q -n PyOpenGL-3.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543766404
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PyOpenGL
cp license.txt %{buildroot}/usr/share/package-licenses/PyOpenGL/license.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyOpenGL/license.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
