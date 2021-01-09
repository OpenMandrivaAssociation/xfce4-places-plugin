%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary: 	A places plugin for the Xfce panel
Name: 		xfce4-places-plugin
Version:	1.8.1
Release:	2
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
Source0: 	http://archive.xfce.org/src/panel-plugins/xfce4-places-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.12
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	perl(XML::Parser)

%description
A places plugin for the Xfce panel.

%prep
%setup -q

%build
%define _disable_ld_no_undefined 1
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog AUTHORS NEWS
%{_bindir}/*
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/places.desktop
