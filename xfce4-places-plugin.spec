Summary: 	A places plugin for the Xfce panel
Name: 		xfce4-places-plugin
Version: 	1.2.0
Release: 	%mkrel 3
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-places-plugin/%{name}-%{version}.tar.bz2
Patch2:		xfce4-places-plugin-1.1.0-format_not_a_string_literal_and_no_format_arguments.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	thunar-devel
Obsoletes:	xfce-places-plugin
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A places plugin for the Xfce panel.

%prep
%setup -q
%patch2 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS
%{_bindir}/*
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/places.desktop
