# Created by pyp2rpm-0.4.2
%global pypi_name jsonschema

Name:           python-%{pypi_name}
Version:	3.0.2
Release:	1
Summary:        An implementation of JSON Schema validation for Python
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/jsonschema
Source0:	https://files.pythonhosted.org/packages/92/d2/8768983d6e4bb1478ea08e7bc186304f47b99c22bfd711caa8e9becb0361/jsonschema-3.0.2.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python2)
BuildRequires:  python2dist(setuptools)
BuildRequires:	python2dist(setuptools-scm)
#BuildRequires:  python2dist(repoze.lru)

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:	python3dist(setuptools-scm)

%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%package -n python2-%{pypi_name}
Summary:	An implementation of JSON Schema validation for Python 2
Group:		Development/Python

Obsoletes:	python-jsonschema < 2.5.1-4
Provides:	python-jsonschema = %{version}-%{release}

%description -n python2-%{pypi_name}
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%prep
%setup -q -n %{pypi_name}-%{version}
%autopatch -p1

# drop bundled egg-info
rm -rf jsonschema.egg-info/

%build
%py2_build
%py3_build

%install
%py3_install
mv %{buildroot}%{_bindir}/jsonschema %{buildroot}%{_bindir}/jsonschema3

%py2_install

%files -n python2-%{pypi_name}
%doc README.rst COPYING
%{python2_sitelib}/%{pypi_name}/
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{_bindir}/jsonschema

%files -n python-%{pypi_name}
%doc README.rst COPYING
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{_bindir}/jsonschema3
