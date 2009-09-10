%define rel 3

Summary: A tool for executing tasks and managing metadata 
Name: bitbake
Version: 1.8.10
Release: %mkrel %rel
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Development/Other
Url: http://bitbake.berlios.de/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python
BuildRequires: python-devel

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
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc AUTHORS  ChangeLog 
%doc contrib
%_bindir/*
%_datadir/%name/
%py_puresitedir/bb/
%py_puresitedir/*.egg-info
