Summary:	GNOME Settings Daemon
Summary(pl.UTF-8):	Demon ustawień GNOME
Name:		gnome-settings-daemon
Version:	2.32.1
Release:	2
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-settings-daemon/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	6420706542e8fb959acba7e2a69ee35f
Patch0:		%{name}-pa-reconnect.patch
Patch1:		%{name}-libnotify.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-desktop-devel >= 2.30.0
BuildRequires:	gtk+2-devel >= 2:2.22.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libgnomekbd-devel >= 2.32.0
BuildRequires:	libnotify-devel >= 0.4.5
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.91
BuildRequires:	pulseaudio-devel >= 0.9.15
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libXxf86misc-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
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
Summary(pl.UTF-8):	Plik nagłówkowy do tworzenia klientów demona ustawień GNOME
Group:		Development/Libraries
Requires:	dbus-glib-devel >= 0.74
Requires:	glib2-devel >= 1:2.20.0
# doesn't require base currently

%description devel
Header file for developing GNOME Settings Daemon clients.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia klientów demona ustawień GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-2.0/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_gnome_settings_daemon_housekeeping.schemas
%gconf_schema_install apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_install apps_gnome_settings_daemon_xrandr.schemas
%gconf_schema_install desktop_gnome_font_rendering.schemas
%gconf_schema_install desktop_gnome_keybindings.schemas
%gconf_schema_install desktop_gnome_peripherals_smartcard.schemas
%gconf_schema_install desktop_gnome_peripherals_touchpad.schemas
%gconf_schema_install gnome-settings-daemon.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall apps_gnome_settings_daemon_housekeeping.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_xrandr.schemas
%gconf_schema_uninstall desktop_gnome_font_rendering.schemas
%gconf_schema_uninstall desktop_gnome_keybindings.schemas
%gconf_schema_uninstall desktop_gnome_peripherals_smartcard.schemas
%gconf_schema_uninstall desktop_gnome_peripherals_touchpad.schemas
%gconf_schema_uninstall gnome-settings-daemon.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
/etc/dbus-1/system.d/org.gnome.SettingsDaemon.DateTimeMechanism.conf
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_housekeeping.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_keybindings.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_xrandr.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_font_rendering.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_keybindings.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_smartcard.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_touchpad.schemas
%{_sysconfdir}/gconf/schemas/gnome-settings-daemon.schemas
%{_sysconfdir}/xdg/autostart/gnome-settings-daemon.desktop
%{_datadir}/dbus-1/system-services/org.gnome.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/gnome-control-center/keybindings/50-accessibility.xml
%{_datadir}/polkit-1/actions/org.gnome.settingsdaemon.datetimemechanism.policy
%attr(755,root,root) %{_libexecdir}/gnome-settings-daemon
%attr(755,root,root) %{_libexecdir}/gsd-locate-pointer
%attr(755,root,root) %{_libexecdir}/gsd-datetime-mechanism
%dir %{_libdir}/gnome-settings-daemon-2.0
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/liba11y-keyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libbackground.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libclipboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libfont.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libhousekeeping.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libkeybindings.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libkeyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libmedia-keys.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libmouse.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libsmartcard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libsound.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libtyping-break.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libxrandr.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libxrdb.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-2.0/libxsettings.so
%{_libdir}/gnome-settings-daemon-2.0/a11y-keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/background.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/clipboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/font.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/housekeeping.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/keybindings.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/media-keys.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/mouse.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-2.0/smartcard.gnome-settings-plugin
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
