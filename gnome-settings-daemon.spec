Summary:	GNOME Settings Daemon
Summary(pl.UTF-8):	Demon ustawień GNOME
Name:		gnome-settings-daemon
Version:	2.21.90.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-settings-daemon/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	6e6146e8f6e2813247ff5aede4ee3dcc
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.21.90
BuildRequires:	alsa-lib-devel >= 1.0.12
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	esound-devel >= 1:0.2.28
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.15.4
BuildRequires:	gnome-desktop-devel >= 2.21.90
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:2.12.5
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomekbd-devel >= 2.21.4
BuildRequires:	libgnomeui-devel >= 2.21.90
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 3.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXxf86misc-devel
Requires(post,preun):	GConf2
Requires:	gnome-vfs2 >= 2.20.0
# It's really needed?
Requires:	gstreamer-audio-effects-base >= 0.10.10
Requires:	libgnomeui >= 2.21.90
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
GNOME Settings Daemon.

%description -l pl.UTF-8
Demon ustawień GNOME.

%package devel
Summary:	Header file for developing GNOME Settings Daemon clients
Summary(pl.UTF-8):	Plik nagłówkowy do tworzenia klientów demona ustawiń GNOME
Group:		Development/Libraries
Requires:	dbus-glib-devel >= 0.74
Requires:	glib2-devel >= 1:2.15.4
# doesn't require base currently

%description devel
Header file for developing GNOME Settings Daemon clients.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia klientów demona ustawiń GNOME.

%prep
%setup -q

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv po/sr@{Latn,latin}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gstreamer=0.10 \
	X_EXTRA_LIBS="-lXext"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon/plugins/*/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_gnome_settings_daemon_default_editor.schemas
%gconf_schema_install apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_install apps_gnome_settings_daemon_screensaver.schemas
%gconf_schema_install desktop_gnome_font_rendering.schemas
%gconf_schema_install gnome-settings-daemon.schemas

%preun
%gconf_schema_uninstall apps_gnome_settings_daemon_default_editor.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_screensaver.schemas
%gconf_schema_uninstall desktop_gnome_font_rendering.schemas
%gconf_schema_uninstall gnome-settings-daemon.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_default_editor.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_keybindings.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_screensaver.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_font_rendering.schemas
%{_sysconfdir}/gconf/schemas/gnome-settings-daemon.schemas
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gnome-settings-daemon
%dir %{_libexecdir}/plugins
%dir %{_libexecdir}/plugins/a11y-keyboard
%attr(755,root,root) %{_libexecdir}/plugins/a11y-keyboard/*.so
%{_libexecdir}/plugins/a11y-keyboard/*-plugin
%dir %{_libexecdir}/plugins/background
%attr(755,root,root) %{_libexecdir}/plugins/background/*.so
%{_libexecdir}/plugins/background/*-plugin
%dir %{_libexecdir}/plugins/clipboard
%attr(755,root,root) %{_libexecdir}/plugins/clipboard/*.so
%{_libexecdir}/plugins/clipboard/*-plugin
%dir %{_libexecdir}/plugins/default-editor
%attr(755,root,root) %{_libexecdir}/plugins/default-editor/*.so
%{_libexecdir}/plugins/default-editor/*-plugin
%dir %{_libexecdir}/plugins/dummy
%attr(755,root,root) %{_libexecdir}/plugins/dummy/*.so
%{_libexecdir}/plugins/dummy/*-plugin
%dir %{_libexecdir}/plugins/font
%attr(755,root,root) %{_libexecdir}/plugins/font/*.so
%{_libexecdir}/plugins/font/*-plugin
%dir %{_libexecdir}/plugins/keybindings
%attr(755,root,root) %{_libexecdir}/plugins/keybindings/*.so
%{_libexecdir}/plugins/keybindings/*-plugin
%dir %{_libexecdir}/plugins/keyboard
%attr(755,root,root) %{_libexecdir}/plugins/keyboard/*.so
%{_libexecdir}/plugins/keyboard/*.glade
%{_libexecdir}/plugins/keyboard/*-plugin
%dir %{_libexecdir}/plugins/media-keys
%attr(755,root,root) %{_libexecdir}/plugins/media-keys/*.so
%{_libexecdir}/plugins/media-keys/*.glade
%{_libexecdir}/plugins/media-keys/*.png
%{_libexecdir}/plugins/media-keys/*-plugin
%dir %{_libexecdir}/plugins/mouse
%attr(755,root,root) %{_libexecdir}/plugins/mouse/*.so
%{_libexecdir}/plugins/mouse/*-plugin
%dir %{_libexecdir}/plugins/screensaver
%attr(755,root,root) %{_libexecdir}/plugins/screensaver/*.so
%{_libexecdir}/plugins/screensaver/*-plugin
%dir %{_libexecdir}/plugins/sound
%attr(755,root,root) %{_libexecdir}/plugins/sound/*.so
%{_libexecdir}/plugins/sound/*-plugin
%dir %{_libexecdir}/plugins/typing-break
%attr(755,root,root) %{_libexecdir}/plugins/typing-break/*.so
%{_libexecdir}/plugins/typing-break/*-plugin
%dir %{_libexecdir}/plugins/xrandr
%attr(755,root,root) %{_libexecdir}/plugins/xrandr/*.so
%{_libexecdir}/plugins/xrandr/*-plugin
%dir %{_libexecdir}/plugins/xrdb
%attr(755,root,root) %{_libexecdir}/plugins/xrdb/*.so
%{_libexecdir}/plugins/xrdb/*-plugin
%dir %{_libexecdir}/plugins/xsettings
%attr(755,root,root) %{_libexecdir}/plugins/xsettings/*.so
%{_libexecdir}/plugins/xsettings/*-plugin
%{_datadir}/gnome-settings-daemon
%{_datadir}/dbus-1/services/*.service

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-settings-daemon-2.0
%{_pkgconfigdir}/gnome-settings-daemon.pc
