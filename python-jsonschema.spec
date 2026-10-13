%define module jsonschema

Name:		python-jsonschema
Version:	4.26.0
Release:	2
Summary:	An implementation of JSON Schema validation for Python
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/jsonschema/
Source0:	https://files.pythonhosted.org/packages/source/j/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	git-core

%description
An implementation of JSON Schema validation for Python

%prep -a
# Requires a checkout of the JSON-Schema-Test-Suite
# https://github.com/json-schema-org/JSON-Schema-Test-Suite
rm jsonschema/tests/test_jsonschema_test_suite.py

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%files
%{_bindir}/%{module}
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
