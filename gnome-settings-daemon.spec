Summary:	GNOME Settings Daemon
Summary(pl.UTF-8):	Demon ustawień GNOME
Name:		gnome-settings-daemon
Version:	3.30.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-settings-daemon/3.30/%{name}-%{version}.tar.xz
# Source0-md5:	ac4cf0cf54d60c839698cad6560367ff
URL:		http://www.gnome.org/
BuildRequires:	NetworkManager-devel >= 1.0
BuildRequires:	alsa-lib-devel
BuildRequires:	colord-devel >= 1.0.2
BuildRequires:	cups-devel >= 1.4
BuildRequires:	fontconfig-devel
BuildRequires:	geoclue2-devel >= 2.3.1
BuildRequires:	geocode-glib-devel >= 3.10.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gnome-desktop-devel >= 3.12.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.24.0
BuildRequires:	gtk+3-devel >= 3.15.3
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libgweather-devel >= 3.10.0
BuildRequires:	libnotify-devel >= 0.7.3
BuildRequires:	librsvg-devel >= 2.36.2
%ifnarch s390 s390x
BuildRequires:	libwacom-devel >= 0.7
%endif
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.44.0
BuildRequires:	nss-devel >= 1:3.11.2
BuildRequires:	pango-devel >= 1:1.20.0
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.113-4
BuildRequires:	pulseaudio-devel >= 2.0
BuildRequires:	rpmbuild(macros) >= 1.593
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel >= 0.99.0
# wayland-client
BuildRequires:	wayland-devel
%ifnarch s390 s390x
BuildRequires:	xorg-driver-input-wacom-devel
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.54.0
Requires:	colord >= 1.0.2
Requires:	cups-lib >= 1.4
Requires:	geoclue2 >= 2.3.1
Requires:	geocode-glib >= 3.10.0
Requires:	gnome-desktop >= 3.12.0
Requires:	gsettings-desktop-schemas >= 3.24.0
Requires:	gtk+3 >= 3.15.3
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	lcms2 >= 2.2
Requires:	libgweather >= 3.10.0
Requires:	libnotify >= 0.7.3
Requires:	librsvg >= 2.36.2
%ifnarch s390 s390x
Requires:	libwacom >= 0.7
%endif
Requires:	nss >= 1:3.11.2
Requires:	pango >= 1:1.20.0
Requires:	polkit-libs >= 0.103
Requires:	pulseaudio-libs >= 2.0
Requires:	upower-libs >= 0.99.0
# sr@Latn vs. sr@latin
Obsoletes:	gnome-settings-daemon-test < 1:3.24.0
Obsoletes:	gnome-settings-daemon-updates < 1:3.14.0
Conflicts:	glibc-misc < 6:2.7
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
Requires:	glib2-devel >= 1:2.54.0
# doesn't require base currently

%description devel
Header file for developing GNOME Settings Daemon clients.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia klientów demona ustawień GNOME.

%prep
%setup -q

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/gtk-modules

%meson_install -C build

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
%attr(755,root,root) %{_libexecdir}/gsd-clipboard
%attr(755,root,root) %{_libexecdir}/gsd-color
%attr(755,root,root) %{_libexecdir}/gsd-datetime
%attr(755,root,root) %{_libexecdir}/gsd-dummy
%attr(755,root,root) %{_libexecdir}/gsd-housekeeping
%attr(755,root,root) %{_libexecdir}/gsd-keyboard
%attr(755,root,root) %{_libexecdir}/gsd-locate-pointer
%attr(755,root,root) %{_libexecdir}/gsd-media-keys
%attr(755,root,root) %{_libexecdir}/gsd-mouse
%attr(755,root,root) %{_libexecdir}/gsd-power
%attr(755,root,root) %{_libexecdir}/gsd-print-notifications
%attr(755,root,root) %{_libexecdir}/gsd-printer
%attr(755,root,root) %{_libexecdir}/gsd-rfkill
%attr(755,root,root) %{_libexecdir}/gsd-screensaver-proxy
%attr(755,root,root) %{_libexecdir}/gsd-sharing
%attr(755,root,root) %{_libexecdir}/gsd-smartcard
%attr(755,root,root) %{_libexecdir}/gsd-sound
%attr(755,root,root) %{_libexecdir}/gsd-test-input-helper
%attr(755,root,root) %{_libexecdir}/gsd-wacom
%attr(755,root,root) %{_libexecdir}/gsd-xsettings
%ifnarch s390 s390x
%attr(755,root,root) %{_libexecdir}/gsd-wacom-led-helper
%attr(755,root,root) %{_libexecdir}/gsd-wacom-oled-helper
%endif
%dir %{_libdir}/gnome-settings-daemon-3.0
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libgsd.so
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
/lib/udev/rules.d/61-gnome-settings-daemon-rfkill.rules
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.*.xml
%{_datadir}/gnome-settings-daemon
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
%ifnarch s390 s390x
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%endif
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.A11ySettings.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Clipboard.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Color.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Datetime.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Housekeeping.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Keyboard.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.MediaKeys.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Mouse.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Power.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.PrintNotifications.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Rfkill.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.ScreensaverProxy.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Sharing.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Smartcard.desktop
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Sound.desktop
%ifnarch s390 s390x
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.Wacom.desktop
%endif
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.XSettings.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-settings-daemon-3.0
%{_pkgconfigdir}/gnome-settings-daemon.pc
