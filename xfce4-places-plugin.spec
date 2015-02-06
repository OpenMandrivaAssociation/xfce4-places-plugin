%define url_ver %(echo %{version} | cut -c 1-3)

Summary: 	A places plugin for the Xfce panel
Name: 		xfce4-places-plugin
Version: 	1.6.0
Release: 	2
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
Source0: 	http://archive.xfce.org/src/panel-plugins/xfce4-places-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfcegui4-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.8.0
BuildRequires:	perl(XML::Parser)

%description
A places plugin for the Xfce panel.

%prep
%setup -q

%build
%configure
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
