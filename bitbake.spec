Summary: A tool for executing tasks and managing metadata 
Name: bitbake
Version: 1.12.0
Release: %mkrel 1
Source0: http://download.berlios.de/%{name}/%{name}-%{version}.tar.gz
License: GPL
Group: Development/Other
Url: http://bitbake.berlios.de/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python
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
%__python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%__python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS ChangeLog 
%doc contrib
%doc %{_docdir}/%{name}-%{version}
%_bindir/*
%_datadir/%name/
%py_puresitedir/codegen.py
%py_puresitedir/bb/
%py_puresitedir/*.egg-info
