#
# Conditional build:
%bcond_without	tests	# unit tests (disable to bootstrap fontParts and booleanOperations)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Classes implementing the pen protocol for manipulating glyphs
Summary(pl.UTF-8):	Klasy implementujące protokół pióra do operacji na glifach
Name:		python-fontPens
Version:	0.2.4
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/fontpens/
Source0:	https://files.pythonhosted.org/packages/source/f/fontpens/fontPens-%{version}.zip
# Source0-md5:	ba666ed73e00da7ba2c84600b4bdeca0
URL:		https://pypi.org/project/fontpens/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-fontParts >= 0.8.1
BuildRequires:	python-fonttools >= 3.32.0
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-fontParts >= 0.8.1
BuildRequires:	python3-fonttools >= 3.32.0
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of classes implementing the pen protocol for manipulating
glyphs.

%description -l pl.UTF-8
Zbiór klas implementujących protokół pióra do operacji na glifach.

%package -n python3-fontPens
Summary:	Classes implementing the pen protocol for manipulating glyphs
Summary(pl.UTF-8):	Klasy implementujące protokół pióra do operacji na glifach
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-fontPens
A collection of classes implementing the pen protocol for manipulating
glyphs.

%description -n python3-fontPens -l pl.UTF-8
Zbiór klas implementujących protokół pióra do operacji na glifach.

%prep
%setup -q -n fontPens-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest Lib/fontPens
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest Lib/fontPens
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py_sitescriptdir}/fontPens
%{py_sitescriptdir}/fontPens-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-fontPens
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/fontPens
%{py3_sitescriptdir}/fontPens-%{version}-py*.egg-info
%endif
