Summary:	A tool for executing tasks and managing metadata 
Name:		bitbake
Version:	1.12.0
Release:	1
Source0:	%{name}-%{version}.tar.gz
License:	GPL
Group:		Development/Other
Url:		http://www.openembedded.org/wiki/BitBake
BuildArch:	noarch
Requires:	python
BuildRequires:	libxml2-utils
BuildRequires:	python-ply
BuildRequires:	python-devel
BuildRequires:	xsltproc

%description
BitBake is, at its simplest, a tool for executing tasks and managing metadata. 
As such, its similarities to GNU make and other build tools are readily 
apparent. It was inspired by Portage, the package management system used 
by the Gentoo Linux distribution. BitBake is the basis of the OpenEmbedded 
project, which is being used to build and maintain a number of embedded 
Linux distributions, including OpenZaurus and Familiar.

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
%{py_puresitedir}/*.egg-info
