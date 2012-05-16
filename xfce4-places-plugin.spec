Summary:	A places plugin for the Xfce panel
Name:		xfce4-places-plugin
Version:	1.3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-places-plugin/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	thunar-vfs-devel
Obsoletes:	xfce-places-plugin

%description
A places plugin for the Xfce panel.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc ChangeLog AUTHORS NEWS
%{_bindir}/*
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/places.desktop
