Summary:	A places plugin for the Xfce panel
Name:		xfce4-places-plugin
Version:	1.3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-places-plugin/%{name}-%{version}.tar.bz2
Patch0:		xfce4-places-plugin-1.2.0-add-support-for-new-exo.patch
Patch2:		xfce4-places-plugin-1.1.0-format_not_a_string_literal_and_no_format_arguments.patch
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	thunar-vfs-devel
Obsoletes:	xfce-places-plugin

%description
A places plugin for the Xfce panel.

%prep
%setup -q
%patch0 -p1
%patch2 -p1

%build
#(tpg) needed for patch0
xdt-autogen
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
