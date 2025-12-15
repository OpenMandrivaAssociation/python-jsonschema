Name:		python-jsonschema
Version:	4.25.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/j/jsonschema/jsonschema-%{version}.tar.gz
Summary:	An implementation of JSON Schema validation for Python
URL:		https://pypi.org/project/jsonschema/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	git-core
BuildArch:	noarch

%description
An implementation of JSON Schema validation for Python

%prep -a
# Requires a checkout of the JSON-Schema-Test-Suite
# https://github.com/json-schema-org/JSON-Schema-Test-Suite
rm jsonschema/tests/test_jsonschema_test_suite.py

# SCM version detection seems to be broken
echo "__version__='%{version}'" >VERSION.py
sed -i -e 's,source = "vcs",path = "VERSION.py",' pyproject.toml

%files
%{_bindir}/jsonschema
%{py_sitedir}/jsonschema
%{py_sitedir}/jsonschema-*.*-info
