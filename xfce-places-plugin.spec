Summary: 	A places plugin for the Xfce panel
Name: 		xfce-places-plugin
Version: 	1.0.0
Release: 	%mkrel 1
License:	GPL
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-places-plugin/xfce4-places-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4
BuildRequires:	xfce-panel-devel >= 4.4
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	thunar-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A places plugin for the Xfce panel.

%prep
%setup -qn xfce4-places-plugin-%{version}

%build

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang xfce4-places-plugin

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f xfce4-places-plugin.lang
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/places.desktop
