%define module keystoneclient
%define oname python_keystoneclient

Name:		python-keystoneclient
Version:	5.8.0
Release:	1
Summary:	Client Library for OpenStack Identity
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/python-keystoneclient/
Source0:	https://files.pythonhosted.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Python bindings to the OpenStack Identity API (Keystone)
￼
This is a client for the OpenStack Identity API, implemented by the Keystone
team; it contains a Python API (the keystoneclient module) for OpenStack’s
Identity Service. For command line interface support, use OpenStackClient.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{oname}-%{version}*.*-info
