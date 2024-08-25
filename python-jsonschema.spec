Name:		python-jsonschema
Version:	4.23.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/j/jsonschema/jsonschema-%{version}.tar.gz
Summary:	An implementation of JSON Schema validation for Python
URL:		https://pypi.org/project/jsonschema/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	git-core
BuildArch:	noarch

%description
An implementation of JSON Schema validation for Python

%prep
%autosetup -p1 -n jsonschema-%{version}

# Requires a checkout of the JSON-Schema-Test-Suite
# https://github.com/json-schema-org/JSON-Schema-Test-Suite
rm jsonschema/tests/test_jsonschema_test_suite.py

# SCM version detection seems to be broken
echo "__version__='%{version}'" >VERSION.py
sed -i -e 's,source = "vcs",path = "VERSION.py",' pyproject.toml

#----------------------------------------------------------------------

%build
%py_build

%install
%py_install

%files
%{_bindir}/jsonschema
%{py_sitedir}/jsonschema
%{py_sitedir}/jsonschema-*.*-info
