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


%changelog
* Wed Apr 20 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.12.0-1mdv2011.0
+ Revision: 656090
- Update to latest upstream release

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 1.8.18-2mdv2011.0
+ Revision: 590154
- rebuild for python 2.7

* Fri Nov 20 2009 Frederik Himpe <fhimpe@mandriva.org> 1.8.18-1mdv2010.1
+ Revision: 467650
- update to new version 1.8.18

* Thu Sep 17 2009 Michael Scherer <misc@mandriva.org> 1.8.12-1mdv2010.0
+ Revision: 443907
- update to new version 1.8.12

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.8.10-3mdv2010.0
+ Revision: 436823
- rebuild

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 1.8.10-2mdv2009.1
+ Revision: 324166
- rebuild

* Mon Feb 11 2008 Michael Scherer <misc@mandriva.org> 1.8.10-1mdv2008.1
+ Revision: 165071
- new version
- use .gz instead of recompressing tarball

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Michael Scherer <misc@mandriva.org> 1.8.8-1mdv2008.0
+ Revision: 80045
- new version 1.8.8

* Sun Jul 08 2007 Michael Scherer <misc@mandriva.org> 1.8.6-1mdv2008.0
+ Revision: 49746
- 1.8.6

* Tue May 01 2007 Michael Scherer <misc@mandriva.org> 1.8.2-1mdv2008.0
+ Revision: 19917
- upgrade to 1.8.2

* Sun Apr 22 2007 Michael Scherer <misc@mandriva.org> 1.8.0-1mdv2008.0
+ Revision: 16763
- Import bitbake

