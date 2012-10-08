# TODO
# - (gnome-settings-daemon:8918): updates-plugin-WARNING **: failed to open directory: Error opening directory '/run/udev/firmware-missing': Permission denied
#
# Conditiional build:
%bcond_with	ibus		# ibus support need no yet released ibus 1.5 or at least devel 1.4.99 version
%bcond_without	packagekit	# packagekit 0.8.x doesn not supports poldek yet
%bcond_without	systemd 	# by default use systemd for session tracking instead of ConsoleKit (fallback to ConsoleKit on runtime)
#
Summary:	GNOME Settings Daemon
Summary(pl.UTF-8):	Demon ustawień GNOME
Name:		gnome-settings-daemon
Version:	3.6.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-settings-daemon/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	27ea0c6ee61a1b3cb5d8e3e0cd10107c
Patch0:		%{name}-pa-reconnect.patch
Patch1:		%{name}-link.patch
Patch2:		systemd-fallback.patch
URL:		http://www.gnome.org/
%{?with_packagekit:BuildRequires:	PackageKit-devel >= 0.8.0}
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	colord-devel >= 0.1.12
BuildRequires:	cups-devel
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-desktop-devel >= 3.6.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.6.0
BuildRequires:	gtk+3-devel >= 3.4.0
%{?with_ibus:BuildRequires:	ibus-devel >= 1.4.99}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libnotify-devel >= 0.7.3
BuildRequires:	libtool
BuildRequires:	libwacom-devel >= 0.6
BuildRequires:	nss-devel >= 3.11.2
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.16
BuildRequires:	rpmbuild(macros) >= 1.593
BuildRequires:	sed >= 4.0
%{?with_systemd:BuildRequires:  systemd-devel}
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel >= 0.9.11
BuildRequires:	xorg-driver-input-wacom-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.32.0
Requires:	gnome-desktop >= 3.6.0
Requires:	gsettings-desktop-schemas >= 3.6.0
Requires:	gtk+3 >= 3.4.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
# sr@Latn vs. sr@latin
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
Requires:	dbus-devel >= 1.2.0
Requires:	glib2-devel >= 1:2.32.0
# doesn't require base currently

%description devel
Header file for developing GNOME Settings Daemon clients.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia klientów demona ustawień GNOME.

%package updates
Summary:	Updates plugin for GNOME Settings Daemon
Group:		Libraries
Requires:       %{name} = %{version}-%{release}

%description updates
Updates plugin for GNOME Settings Daemon.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{?with_systemd:%patch2 -p1}

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{__enable_disable systemd systemd} \
	%{__enable_disable packagekit packagekit} \
	%{__enable_disable ibus ibus} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/gtk-modules

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libexecdir}/gnome-fallback-mount-helper
%attr(755,root,root) %{_libexecdir}/gnome-settings-daemon
%attr(755,root,root) %{_libexecdir}/gsd-backlight-helper
%attr(755,root,root) %{_libexecdir}/gsd-input-sources-switcher
%attr(755,root,root) %{_libexecdir}/gsd-locate-pointer
%attr(755,root,root) %{_libexecdir}/gsd-printer
%attr(755,root,root) %{_libexecdir}/gsd-wacom-led-helper
%dir %{_libdir}/gnome-settings-daemon-3.0
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/liba11y-keyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/liba11y-settings.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libbackground.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libclipboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libcolor.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libcursor.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libgsd.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libgsdwacom.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libhousekeeping.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libkeyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libmedia-keys.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libmouse.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/liborientation.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libpower.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libprint-notifications.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libsmartcard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libsound.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libxrandr.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libxsettings.so
%{_libdir}/gnome-settings-daemon-3.0/a11y-keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/a11y-settings.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/background.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/clipboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/color.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/cursor.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/housekeeping.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/media-keys.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/mouse.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/orientation.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/power.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/print-notifications.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/smartcard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/sound.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/wacom.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/xrandr.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/xsettings.gnome-settings-plugin
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-settings-daemon
%{_datadir}/gnome-settings-daemon-3.0
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/gnome-settings-daemon.1*
%{_sysconfdir}/xdg/autostart/gnome-fallback-mount-helper.desktop
%{_sysconfdir}/xdg/autostart/gnome-settings-daemon.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gsd-list-wacom
%attr(755,root,root) %{_libexecdir}/gsd-test-a11y-keyboard
%attr(755,root,root) %{_libexecdir}/gsd-test-a11y-settings
%attr(755,root,root) %{_libexecdir}/gsd-test-background
%attr(755,root,root) %{_libexecdir}/gsd-test-input-helper
%attr(755,root,root) %{_libexecdir}/gsd-test-keyboard
%attr(755,root,root) %{_libexecdir}/gsd-test-media-keys
%attr(755,root,root) %{_libexecdir}/gsd-test-mouse
%attr(755,root,root) %{_libexecdir}/gsd-test-orientation
%attr(755,root,root) %{_libexecdir}/gsd-test-power
%attr(755,root,root) %{_libexecdir}/gsd-test-print-notifications
%attr(755,root,root) %{_libexecdir}/gsd-test-smartcard
%attr(755,root,root) %{_libexecdir}/gsd-test-sound
%attr(755,root,root) %{_libexecdir}/gsd-test-wacom
%attr(755,root,root) %{_libexecdir}/gsd-test-xsettings
%{_includedir}/gnome-settings-daemon-3.0
%{_pkgconfigdir}/gnome-settings-daemon.pc

%if %{with packagekit}
%files updates
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libupdates.so
%{_libdir}/gnome-settings-daemon-3.0/updates.gnome-settings-plugin
%{_datadir}/dbus-1/interfaces/org.gnome.SettingsDaemonUpdates.xml
%endif
