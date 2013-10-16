%define url_ver %(echo %{version} | cut -c 1-3)

Summary: 	A places plugin for the Xfce panel
Name: 		xfce4-places-plugin
Version: 	1.5.0
Release: 	3
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
Source0: 	http://archive.xfce.org/src/panel-plugins/xfce4-places-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfcegui4-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.8.0
BuildRequires:	perl(XML::Parser)
BuildRequires:	thunar-vfs-devel

%description
A places plugin for the Xfce panel.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std 

%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%files -f %{name}.lang
%doc ChangeLog AUTHORS NEWS
%{_bindir}/*
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/places.desktop


%changelog
* Fri Apr 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.0-4mdv2011.0
+ Revision: 660771
- add requires on thunar-vfs-devel
- Patch0: add support for newer exo library

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.0-2mdv2010.1
+ Revision: 543433
- rebuild for mdv 2010.1

* Fri Jul 31 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.0-1mdv2010.0
+ Revision: 405206
- update to new version 1.2.0
- drop patches 0 and as they were merged upstream

* Sun Mar 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-8mdv2009.1
+ Revision: 353058
- Patch2: fix compiling with Werror=format-strings

* Sun Nov 23 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-7mdv2009.1
+ Revision: 306098
- Patch0: nerw version for xfce bugzilla
- Patch1: do not segfault on plugin exit

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-6mdv2009.1
+ Revision: 295004
- rebuild for new Xfce4.6 beta1

* Fri Oct 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-5mdv2009.0
+ Revision: 291579
- Patch0: new version from xfce bugzilla

* Fri Sep 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-4mdv2009.0
+ Revision: 281253
- Patch0: new version of patch

* Tue Aug 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-3mdv2009.0
+ Revision: 273490
- Patch0: use XDG_DESKTOP_DIR environment variable for desktop directory

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-2mdv2009.0
+ Revision: 269791
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-1mdv2009.0
+ Revision: 216760
- update to new version 1.1.0
- package NEWS file

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-2mdv2008.1
+ Revision: 110128
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING file
- use upstream name

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 102239
- update to the final version
- new version

* Sat Aug 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.991-1mdv2008.0
+ Revision: 65407
- new version

* Fri May 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 31038
- Import xfce-places-plugin

