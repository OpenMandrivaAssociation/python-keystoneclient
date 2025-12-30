Name:		python-keystoneclient
Version:	5.5.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/python-keystoneclient/python-keystoneclient-%{version}.tar.gz
Summary:	Client Library for OpenStack Identity
URL:		https://pypi.org/project/keystoneclient/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pbr)
BuildSystem:	python
BuildArch:	noarch

%description
Python bindings to the OpenStack Identity API (Keystone)
￼
This is a client for the OpenStack Identity API, implemented by the Keystone
team; it contains a Python API (the keystoneclient module) for OpenStack’s
Identity Service. For command line interface support, use OpenStackClient.


%files
%{py_sitedir}/keystoneclient
%{py_sitedir}/python_keystoneclient-*.*-info
