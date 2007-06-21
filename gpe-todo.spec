Summary:	GPE todo list
Summary(pl.UTF-8):	Lista rzeczy do zrobienia GPE
Name:		gpe-todo
Version:	0.56
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	d60eda0b82431bc4dd92cf7c40c0efe9
URL:		http://gpe.linuxtogo.org/projects/GPE-todo.shtml
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libgpepimc-devel >= 0.8
BuildRequires:	libgpewidget-devel >= 0.114
BuildRequires:	libtododb-devel
BuildRequires:	pkgconfig
# optional: hildon-libs libosso
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE todo list, for embedded devices.

%description -l pl.UTF-8
Lista rzeczy do zrobienia (todo) GPE dla urządzeń wbudowanych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%dir %{_datadir}/gpe-todo
%{_datadir}/gpe-todo/bar-box.png
%{_datadir}/gpe-todo/dot-box.png
%{_datadir}/gpe-todo/flag-16.png
%{_datadir}/gpe-todo/notick-box.png
%{_datadir}/gpe-todo/tick-box.png
