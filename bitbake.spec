Summary:	A tool for executing tasks and managing metadata 
Name:		bitbake
Version:	1.24.0
Release:	2
# from git://git.openembedded.org/bitbake
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Other
Url:		http://www.openembedded.org/wiki/BitBake
BuildArch:	noarch
Requires:	python
BuildRequires:	libxml2-utils
BuildRequires:	python-ply
BuildRequires:	python-devel
BuildRequires:	xsltproc

%description
BitBake is a make-like build tool with the special focus of distributions and
packages for embedded Linux cross compilation although it is not limited to 
that. It is derived from Portage, which is the package management system used 
by the Gentoo Linux distribution. BitBake existed for some time in the 
OpenEmbedded project until it was separated out into a standalone, maintained,
distribution-independent tool. BitBake is co-maintained by the Yocto Project 
and the OpenEmbedded project.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files 
%doc AUTHORS ChangeLog 
%doc contrib
%doc %{_docdir}/%{name}-%{version}
%{_bindir}/*
%{_datadir}/%{name}/
%{py_puresitedir}/codegen.py
%{py_puresitedir}/bb/
%{py_puresitedir}/prserv
%{py_puresitedir}/*.egg-info
