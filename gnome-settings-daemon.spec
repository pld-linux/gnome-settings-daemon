Summary:	GNOME Settings Daemon
Summary(pl.UTF-8):	Demon ustawień GNOME
Name:		gnome-settings-daemon
Version:	47.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-settings-daemon/47/%{name}-%{version}.tar.xz
# Source0-md5:	39babcea9c9eb5fd7809cbc685cd282c
URL:		https://gitlab.gnome.org/GNOME/gnome-settings-daemon
BuildRequires:	ModemManager-devel >= 1.0
BuildRequires:	NetworkManager-devel >= 1.0
BuildRequires:	alsa-lib-devel
BuildRequires:	colord-devel >= 1.4.5
BuildRequires:	cups-devel >= 1.4
BuildRequires:	fontconfig-devel
BuildRequires:	gcr4-devel >= 4
BuildRequires:	geoclue2-devel >= 2.3.1
BuildRequires:	geocode-glib2-devel >= 3.26.3
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.70
BuildRequires:	gnome-desktop-devel >= 3.37.1
BuildRequires:	gsettings-desktop-schemas-devel >= 46
BuildRequires:	gtk+3-devel >= 3.15.3
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libgweather4-devel >= 4.0
BuildRequires:	libnotify-devel >= 0.7.3
%ifnarch s390 s390x
BuildRequires:	libwacom-devel >= 0.7
%endif
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.57.0
BuildRequires:	ninja >= 1.5
BuildRequires:	nss-devel >= 1:3.11.2
BuildRequires:	pango-devel >= 1:1.20.0
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.114
BuildRequires:	pulseaudio-devel >= 13.0
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
# or libelogind >= 209 (with -Denable_systemd=false)
BuildRequires:	systemd-devel >= 1:243
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel >= 0.99.12
# wayland-client
BuildRequires:	wayland-devel
%ifnarch s390 s390x
BuildRequires:	xorg-driver-input-wacom-devel
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel >= 6.0
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.70
Requires:	colord >= 1.4.5
Requires:	cups-lib >= 1.4
Requires:	gcr4-libs >= 4
Requires:	geoclue2 >= 2.3.1
Requires:	geocode-glib2 >= 3.26.3
Requires:	glib2 >= 1:2.70
Requires:	gnome-desktop >= 3.37.1
Requires:	gsettings-desktop-schemas >= 46
Requires:	gtk+3 >= 3.15.3
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	lcms2 >= 2.2
Requires:	libgweather4 >= 4.0
Requires:	libnotify >= 0.7.3
%ifnarch s390 s390x
Requires:	libwacom >= 0.7
%endif
Requires:	nss >= 1:3.11.2
Requires:	pango >= 1:1.20.0
Requires:	polkit-libs >= 0.114
Requires:	pulseaudio-libs >= 13.0
Requires:	systemd-units >= 1:243
Requires:	upower-libs >= 0.99.12
Requires:	xorg-lib-libXfixes >= 6.0
Obsoletes:	gnome-settings-daemon-test < 1:3.24.0
Obsoletes:	gnome-settings-daemon-updates < 1:3.14.0
Conflicts:	gnome-color-manager < 3.1.92-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Settings Daemon.

%description -l pl.UTF-8
Demon ustawień GNOME.

%package devel
Summary:	Header file for developing GNOME Settings Daemon clients
Summary(pl.UTF-8):	Plik nagłówkowy do tworzenia klientów demona ustawień GNOME
Group:		Development/Libraries
Requires:	glib2-devel >= 1:2.70
# doesn't require base currently

%description devel
Header file for developing GNOME Settings Daemon clients.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia klientów demona ustawień GNOME.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
# differs from libgsd.so path, see meson.build /gsd_gtk_modules_directory
install -d $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/gtk-modules

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libexecdir}/gsd-a11y-settings
%attr(755,root,root) %{_libexecdir}/gsd-backlight-helper
%attr(755,root,root) %{_libexecdir}/gsd-color
%attr(755,root,root) %{_libexecdir}/gsd-datetime
%attr(755,root,root) %{_libexecdir}/gsd-housekeeping
%attr(755,root,root) %{_libexecdir}/gsd-keyboard
%attr(755,root,root) %{_libexecdir}/gsd-media-keys
%attr(755,root,root) %{_libexecdir}/gsd-power
%attr(755,root,root) %{_libexecdir}/gsd-print-notifications
%attr(755,root,root) %{_libexecdir}/gsd-printer
%attr(755,root,root) %{_libexecdir}/gsd-rfkill
%attr(755,root,root) %{_libexecdir}/gsd-screensaver-proxy
%attr(755,root,root) %{_libexecdir}/gsd-sharing
%attr(755,root,root) %{_libexecdir}/gsd-smartcard
%attr(755,root,root) %{_libexecdir}/gsd-sound
%attr(755,root,root) %{_libexecdir}/gsd-usb-protection
%ifnarch s390 s390x
%attr(755,root,root) %{_libexecdir}/gsd-wacom
%attr(755,root,root) %{_libexecdir}/gsd-wacom-oled-helper
%endif
%attr(755,root,root) %{_libexecdir}/gsd-wwan
%attr(755,root,root) %{_libexecdir}/gsd-xsettings
%dir %{_libdir}/gnome-settings-daemon-3.0
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
%dir %{_libdir}/gnome-settings-daemon-47
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-47/libgsd.so
/lib/udev/rules.d/61-gnome-settings-daemon-rfkill.rules
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.*.xml
%{_datadir}/gnome-settings-daemon
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
%ifnarch s390 s390x
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%endif
%dir %{systemduserunitdir}/gnome-session-x11-services.target.wants
%{systemduserunitdir}/gnome-session-x11-services.target.wants/org.gnome.SettingsDaemon.XSettings.service
%dir %{systemduserunitdir}/gnome-session-x11-services-ready.target.wants
%{systemduserunitdir}/gnome-session-x11-services-ready.target.wants/org.gnome.SettingsDaemon.XSettings.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.A11ySettings.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.A11ySettings.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Color.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Color.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Datetime.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Datetime.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Housekeeping.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Housekeeping.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Keyboard.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Keyboard.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.MediaKeys.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.MediaKeys.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Power.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Power.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.PrintNotifications.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.PrintNotifications.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Rfkill.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Rfkill.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.ScreensaverProxy.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.ScreensaverProxy.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Sharing.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Sharing.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Smartcard.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Smartcard.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Sound.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Sound.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.UsbProtection.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.UsbProtection.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Wacom.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Wacom.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.Wwan.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.Wwan.target
%{systemduserunitdir}/org.gnome.SettingsDaemon.XSettings.service
%{systemduserunitdir}/org.gnome.SettingsDaemon.XSettings.target
%dir %{_sysconfdir}/xdg/Xwayland-session.d
%attr(755,root,root) %{_sysconfdir}/xdg/Xwayland-session.d/00-xrdb
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.A11ySettings.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Color.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Datetime.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Housekeeping.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Keyboard.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.MediaKeys.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Power.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.PrintNotifications.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Rfkill.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.ScreensaverProxy.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Sharing.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Smartcard.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Sound.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.UsbProtection.desktop
%ifnarch s390 s390x
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Wacom.desktop
%endif
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Wwan.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.XSettings.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-settings-daemon-47
%{_pkgconfigdir}/gnome-settings-daemon.pc
