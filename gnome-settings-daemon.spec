Summary:	GNOME Settings Daemon
Summary(pl.UTF-8):	Demon ustawień GNOME
Name:		gnome-settings-daemon
Version:	2.27.91
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-settings-daemon/2.27/%{name}-%{version}.tar.bz2
# Source0-md5:	cb5ce91b824bb46031531195f9dbe4c4
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-desktop-devel >= 2.26.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomekbd-devel >= 2.26.0
BuildRequires:	libtool
BuildRequires:	libnotify-devel >= 0.4.5
BuildRequires:	libxklavier-devel >= 4.0
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.12
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXxf86misc-devel
Requires(post,preun):	GConf2
Requires(post,postun):	gtk+2
Requires:	xorg-app-xrdb
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Settings Daemon.

%description -l pl.UTF-8
Demon ustawień GNOME.

%package devel
Summary:	Header file for developing GNOME Settings Daemon clients
Summary(pl.UTF-8):	Plik nagłówkowy do tworzenia klientów demona ustawiń GNOME
Group:		Development/Libraries
Requires:	dbus-glib-devel >= 0.74
Requires:	glib2-devel >= 1:2.20.0
# doesn't require base currently

%description devel
Header file for developing GNOME Settings Daemon clients.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia klientów demona ustawiń GNOME.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-2.0/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_gnome_settings_daemon_housekeeping.schemas
%gconf_schema_install apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_install apps_gnome_settings_daemon_xrandr.schemas
%gconf_schema_install desktop_gnome_font_rendering.schemas
%gconf_schema_install desktop_gnome_keybindings.schemas
%gconf_schema_install desktop_gnome_peripherals_touchpad.schemas
%gconf_schema_install gnome-settings-daemon.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall apps_gnome_settings_daemon_housekeeping.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_xrandr.schemas
%gconf_schema_uninstall desktop_gnome_font_rendering.schemas
%gconf_schema_uninstall desktop_gnome_keybindings.schemas
%gconf_schema_uninstall desktop_gnome_peripherals_touchpad.schemas
%gconf_schema_uninstall gnome-settings-daemon.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_housekeeping.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_keybindings.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_xrandr.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_font_rendering.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_keybindings.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_touchpad.schemas
%{_sysconfdir}/gconf/schemas/gnome-settings-daemon.schemas
%{_sysconfdir}/xdg/autostart/gnome-settings-daemon.desktop
%{_datadir}/gnome-control-center/keybindings/50-accessibility.xml
%attr(755,root,root) %{_libdir}/gnome-settings-daemon
%dir %{_libdir}/gnome-settings-daemon-2.0
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/liba11y-keyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libbackground.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libclipboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libdummy.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libfont.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libhousekeeping.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libkeybindings.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libkeyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libmedia-keys.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libmouse.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libsound.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libtyping-break.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libxrandr.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libxrdb.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libxsettings.so
%{_libdir}/gnome-settings-daemon-2.0/a11y-keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/background.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/clipboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/dummy.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/font.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/housekeeping.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/keybindings.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/media-keys.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/mouse.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/sound.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/typing-break.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/xrandr.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/xrdb.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/xsettings.gnome-settings-plugin
%{_datadir}/gnome-settings-daemon
%{_datadir}/dbus-1/services/org.gnome.SettingsDaemon.service
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-settings-daemon-2.0
%{_pkgconfigdir}/gnome-settings-daemon.pc
