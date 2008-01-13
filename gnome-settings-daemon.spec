Summary:	GNOME Settings Daemon
Summary(pl.UTF-8):	Demon ustawień GNOME
Name:		gnome-settings-daemon
Version:	2.21.4
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-settings-daemon/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	e4c6834638df22bceeeb11d3af9c2021
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	alsa-lib-devel >= 1.0.12
BuildRequires:	audiofile >= 1:0.2.6
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	esound-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.13.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomekbd-devel >= 2.21.4
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 3.3
BuildRequires:	libxml2-devel >= 1:2.6.30
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXxf86misc-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gnome-vfs2 >= 2.20.0
Requires:	gstreamer-audio-effects-base >= 0.10.10
Requires:	libgnomeui >= 2.20.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Settings Daemon.

%description -l pl.UTF-8
Demon ustawień GNOME.

%package devel
Summary:	Header file for developing GNOME Settings Daemon clients
Summary(pl.UTF-8):	Plik nagłówkowy do tworzenia klientów demona ustawiń GNOME
Group:		Development/Libraries
Requires:	dbus-glib-devel >= 0.73
Requires:	glib2-devel >= 1:2.13.0
# doesn't require base currently

%description devel
Header file for developing GNOME Settings Daemon clients.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia klientów demona ustawiń GNOME.

%prep
%setup -q

%build
%{__gnome_doc_prepare}
%{__gnome_doc_common}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gstreamer=0.10 \
	--enable-aboutme \
	X_EXTRA_LIBS="-lXext"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/window-manager-settings/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions*/*.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_gnome_settings_daemon_default.schemas
%gconf_schema_install apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_install apps_gnome_settings_daemon_screensaver.schemas
%gconf_schema_install desktop_gnome_font_rendering.schemas
%gconf_schema_install gnome-settings-daemon.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall apps_gnome_settings_daemon_default.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_keybindings.schemas
%gconf_schema_uninstall apps_gnome_settings_daemon_screensaver.schemas
%gconf_schema_uninstall desktop_gnome_font_rendering.schemas
%gconf_schema_uninstall gnome-settings-daemon.schemas

%postun
%scrollkeeper_update_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_default_editor.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_keybindings.schemas
%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_screensaver.schemas
%{_sysconfdir}/gconf/schemas/desktop_gnome_font_rendering.schemas
%{_sysconfdir}/gconf/schemas/gnome-settings-daemon.schemas
%dir %{_libdir}/gnome-settings-daemon
%attr(755,root,root) %{_libexecdir}/gnome-settings-daemon/gnome-settings-daemon
%dir %{_libdir}/gnome-settings-daemon/plugins
%dir %{_libdir}/gnome-settings-daemon/plugins/a11y-keyboard
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/a11y-keyboard/*.so
%{_libdir}/gnome-settings-daemon/plugins/a11y-keyboard/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/background
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/background/*.so
%{_libdir}/gnome-settings-daemon/plugins/background/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/clipboard
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/clipboard/*.so
%{_libdir}/gnome-settings-daemon/plugins/clipboard/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/default-editor
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/default-editor/*.so
%{_libdir}/gnome-settings-daemon/plugins/default-editor/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/dummy
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/dummy/*.so
%{_libdir}/gnome-settings-daemon/plugins/dummy/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/font
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/font/*.so
%{_libdir}/gnome-settings-daemon/plugins/font/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/keybindings
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/keybindings/*.so
%{_libdir}/gnome-settings-daemon/plugins/keybindings/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/keyboard
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/keyboard/*.so
%{_libdir}/gnome-settings-daemon/plugins/keyboard/*.glade
%{_libdir}/gnome-settings-daemon/plugins/keyboard/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/media-keys
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/media-keys/*.so
%{_libdir}/gnome-settings-daemon/plugins/media-keys/*.glade
%{_libdir}/gnome-settings-daemon/plugins/media-keys/*.png
%{_libdir}/gnome-settings-daemon/plugins/media-keys/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/mouse
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/mouse/*.so
%{_libdir}/gnome-settings-daemon/plugins/mouse/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/screensaver
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/screensaver/*.so
%{_libdir}/gnome-settings-daemon/plugins/screensaver/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/sound
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/sound/*.so
%{_libdir}/gnome-settings-daemon/plugins/sound/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/typing-break
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/typing-break/*.so
%{_libdir}/gnome-settings-daemon/plugins/typing-break/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/xrandr
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/xrandr/*.so
%{_libdir}/gnome-settings-daemon/plugins/xrandr/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/xrdb
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/xrdb/*.so
%{_libdir}/gnome-settings-daemon/plugins/xrdb/*-plugin
%dir %{_libdir}/gnome-settings-daemon/plugins/xsettings
%attr(755,root,root) %{_libdir}/gnome-settings-daemon/plugins/xsettings/*.so
%{_libdir}/gnome-settings-daemon/plugins/xsettings/*-plugin
%{_datadir}/gnome-settings-daemon
%{_datadir}/dbus-1/services/*.service

%files devel
%defattr(644,root,root,755)
%{_includedir}/gnome-settings-daemon-2.0
%{_pkgconfigdir}/gnome-settings-daemon.pc
