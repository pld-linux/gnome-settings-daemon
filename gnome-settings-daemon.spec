# TODO
# - (gnome-settings-daemon:8918): updates-plugin-WARNING **: failed to open directory: Error opening directory '/run/udev/firmware-missing': Permission denied
#
# Conditiional build:
%bcond_without	ibus		# ibus support
%bcond_without	packagekit	# PackageKit support
#
Summary:	GNOME Settings Daemon
Summary(pl.UTF-8):	Demon ustawień GNOME
Name:		gnome-settings-daemon
Version:	3.12.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-settings-daemon/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	9bafed3afd490078967fcf78de5d23f6
URL:		http://www.gnome.org/
%{?with_packagekit:BuildRequires:	PackageKit-devel >= 0.8.1}
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	colord-devel >= 1.0.2
BuildRequires:	cups-devel >= 1.4
BuildRequires:	fontconfig-devel
BuildRequires:	geoclue2-devel >= 2.1.2
BuildRequires:	geocode-glib-devel >= 3.10.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gnome-desktop-devel >= 3.12.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.10.0
BuildRequires:	gtk+3-devel >= 3.8.0
%{?with_ibus:BuildRequires:	ibus-devel >= 1.4.99}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	lcms2-devel >= 2.2
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libgweather-devel >= 3.10.0
BuildRequires:	libnotify-devel >= 0.7.3
BuildRequires:	librsvg-devel >= 2.36.2
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	libwacom-devel >= 0.7
BuildRequires:	nss-devel >= 3.11.2
BuildRequires:	pango-devel >= 1:1.20.0
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.103
BuildRequires:	pulseaudio-devel >= 2.0
BuildRequires:	rpmbuild(macros) >= 1.593
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel >= 0.99.0
BuildRequires:	xorg-driver-input-wacom-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.38.0
Requires:	colord >= 1.0.2
Requires:	cups-lib >= 1.4
Requires:	geoclue2 >= 2.1.2
Requires:	geocode-glib >= 3.10.0
Requires:	gnome-desktop >= 3.12.0
Requires:	gsettings-desktop-schemas >= 3.10.0
Requires:	gtk+3 >= 3.8.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
%{?with_ibus:Requires:	ibus-libs >= 1.4.99}
Requires:	lcms2 >= 2.2
Requires:	libgweather >= 3.10.0
Requires:	libnotify >= 0.7.3
Requires:	librsvg >= 2.36.2
Requires:	libwacom >= 0.7
Requires:	pango >= 1:1.20.0
Requires:	polkit-libs >= 0.103
Requires:	pulseaudio-libs >= 2.0
Requires:	upower-libs >= 0.99.0
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
Requires:	glib2-devel >= 1:2.38.0
# doesn't require base currently

%description devel
Header file for developing GNOME Settings Daemon clients.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia klientów demona ustawień GNOME.

%package test
Summary:	Test plugins for GNOME Settings Daemon
Summary(pl.UTF-8):	Wtyczki testowe dla demona ustawień GNOME
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description test
Test plugins for GNOME Settings Daemon.

%description test -l pl.UTF-8
Wtyczki testowe dla demona ustawień GNOME.

%package updates
Summary:	Updates plugin for GNOME Settings Daemon
Summary(pl.UTF-8):	Wtyczka uaktualnień dla demona ustawień GNOME
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description updates
Updates plugin for GNOME Settings Daemon.

%description updates -l pl.UTF-8
Wtyczka uaktualnień dla demona ustawień GNOME.

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
%configure \
	%{__enable_disable ibus ibus} \
	%{__enable_disable packagekit packagekit} \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/gtk-modules

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	udevrulesdir=/lib/udev/rules.d

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/*.la

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
%attr(755,root,root) %{_libexecdir}/gnome-settings-daemon
%attr(755,root,root) %{_libexecdir}/gnome-settings-daemon-localeexec
%attr(755,root,root) %{_libexecdir}/gsd-backlight-helper
%attr(755,root,root) %{_libexecdir}/gsd-locate-pointer
%attr(755,root,root) %{_libexecdir}/gsd-printer
%attr(755,root,root) %{_libexecdir}/gsd-test-screensaver-proxy
%attr(755,root,root) %{_libexecdir}/gsd-wacom-led-helper
%attr(755,root,root) %{_libexecdir}/gsd-wacom-oled-helper
%dir %{_libdir}/gnome-settings-daemon-3.0
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/liba11y-keyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/liba11y-settings.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libclipboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libcolor.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libcursor.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libdatetime.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libgsd.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libgsdwacom.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libhousekeeping.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libkeyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libmedia-keys.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libmouse.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/liborientation.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libpower.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libprint-notifications.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/librfkill.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libscreensaver-proxy.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libsmartcard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libsound.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libxrandr.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libxsettings.so
%{_libdir}/gnome-settings-daemon-3.0/a11y-keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/a11y-settings.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/clipboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/color.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/cursor.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/datetime.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/housekeeping.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/media-keys.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/mouse.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/orientation.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/power.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/print-notifications.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/rfkill.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/screensaver-proxy.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/smartcard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/sound.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/wacom.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/xrandr.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/xsettings.gnome-settings-plugin
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
/lib/udev/rules.d/61-gnome-settings-daemon-rfkill.rules
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert
%{_datadir}/dbus-1/services/org.freedesktop.IBus.service
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.*.xml
%{_datadir}/gnome-settings-daemon
%{_datadir}/gnome-settings-daemon-3.0
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%{_iconsdir}/hicolor/*x*/apps/gsd-xrandr.png
%{_iconsdir}/hicolor/scalable/apps/gsd-xrandr.svg
%{_mandir}/man1/gnome-settings-daemon.1*
%{_sysconfdir}/xdg/autostart/gnome-settings-daemon.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-settings-daemon-3.0
%{_pkgconfigdir}/gnome-settings-daemon.pc

%files test
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gsd-list-wacom
%attr(755,root,root) %{_libexecdir}/gsd-test-a11y-keyboard
%attr(755,root,root) %{_libexecdir}/gsd-test-a11y-settings
%attr(755,root,root) %{_libexecdir}/gsd-test-cursor
%attr(755,root,root) %{_libexecdir}/gsd-test-datetime
%attr(755,root,root) %{_libexecdir}/gsd-test-housekeeping
%attr(755,root,root) %{_libexecdir}/gsd-test-input-helper
%attr(755,root,root) %{_libexecdir}/gsd-test-keyboard
%attr(755,root,root) %{_libexecdir}/gsd-test-media-keys
%attr(755,root,root) %{_libexecdir}/gsd-test-mouse
%attr(755,root,root) %{_libexecdir}/gsd-test-orientation
%attr(755,root,root) %{_libexecdir}/gsd-test-print-notifications
%attr(755,root,root) %{_libexecdir}/gsd-test-rfkill
%attr(755,root,root) %{_libexecdir}/gsd-test-smartcard
%attr(755,root,root) %{_libexecdir}/gsd-test-sound
%attr(755,root,root) %{_libexecdir}/gsd-test-updates
%attr(755,root,root) %{_libexecdir}/gsd-test-wacom
%attr(755,root,root) %{_libexecdir}/gsd-test-wacom-osd
%attr(755,root,root) %{_libexecdir}/gsd-test-xrandr
%attr(755,root,root) %{_libexecdir}/gsd-test-xsettings

%if %{with packagekit}
%files updates
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libupdates.so
%{_libdir}/gnome-settings-daemon-3.0/updates.gnome-settings-plugin
%endif
