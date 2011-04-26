Summary:	GNOME Settings Daemon
Summary(pl.UTF-8):	Demon ustawień GNOME
Name:		gnome-settings-daemon
Version:	3.0.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-settings-daemon/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	6407fa30e1f36481d3fe7de50f61d535
Patch0:		%{name}-pa-reconnect.patch
# PLD-specific patches
Patch100:	use-etc-sysconfig-timezone.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	PackageKit-devel >= 0.6.13
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	cups-devel
BuildRequires:	dbus-devel >= 1.2.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-desktop-devel >= 2.91.93
BuildRequires:	gsettings-desktop-schemas-devel >= 2.91.92
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libgnomekbd-devel >= 2.91.5
BuildRequires:	libnotify-devel >= 0.6.1
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 5.0
BuildRequires:	nss-devel >= 3.11.2
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.97
BuildRequires:	pulseaudio-devel >= 0.9.16
BuildRequires:	rpmbuild(macros) >= 1.593
BuildRequires:	sed >= 4.0
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel >= 0.9.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-proto-kbproto-devel
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	gnome-desktop >= 2.91.93
Requires:	gsettings-desktop-schemas >= 2.91.92
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
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
Requires:	dbus-devel >= 1.2.0
Requires:	dbus-glib-devel >= 0.74
Requires:	glib2-devel >= 1:2.26.0
# doesn't require base currently

%description devel
Header file for developing GNOME Settings Daemon clients.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia klientów demona ustawień GNOME.

%prep
%setup -q
%patch0 -p1
%patch100 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
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
%attr(755,root,root) %{_libexecdir}/gnome-settings-daemon
%attr(755,root,root) %{_libexecdir}/gsd-locate-pointer
%attr(755,root,root) %{_libexecdir}/gsd-datetime-mechanism
%attr(755,root,root) %{_libexecdir}/gsd-printer
%dir %{_libdir}/gnome-settings-daemon-3.0
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/liba11y-keyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/liba11y-settings.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libautomount.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libbackground.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libclipboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libhousekeeping.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libkeybindings.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libkeyboard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libmedia-keys.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libmouse.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libprint-notifications.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libsmartcard.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libsound.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libupdates.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libwacom.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libxrandr.so
%attr(755,root,root) %{_libdir}/gnome-settings-daemon-3.0/libxsettings.so
%{_libdir}/gnome-settings-daemon-3.0/a11y-keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/a11y-settings.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/automount.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/background.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/clipboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/housekeeping.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/keybindings.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/media-keys.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/mouse.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/print-notifications.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/smartcard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/sound.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/updates.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/wacom.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/xrandr.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/xsettings.gnome-settings-plugin
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert
%{_datadir}/dbus-1/services/org.gnome.SettingsDaemon.service
%{_datadir}/dbus-1/system-services/org.gnome.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-settings-daemon
%{_datadir}/gnome-settings-daemon-3.0
%{_datadir}/polkit-1/actions/org.gnome.settingsdaemon.datetimemechanism.policy
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/gnome-settings-daemon.1*
%{_sysconfdir}/dbus-1/system.d/org.gnome.SettingsDaemon.DateTimeMechanism.conf
%{_sysconfdir}/xdg/autostart/gnome-settings-daemon.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-settings-daemon-3.0
%{_pkgconfigdir}/gnome-settings-daemon.pc
%{_datadir}/dbus-1/interfaces/org.gnome.SettingsDaemonUpdates.xml
