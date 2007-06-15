#
Summary:	GPE todo list
Name:		gpe-todo
Version:	0.56
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	d60eda0b82431bc4dd92cf7c40c0efe9
URL:		http://gpe.linuxtogo.org
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libgpewidget-devel
BuildRequires:	libtododb-devel
BuildRequires:	sed >= 4.0
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define gpename %(echo %{name} | sed -e 's/gpe-//')

%description
GPE todo list, for embedded devices

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
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%dir %{_datadir}/gpe-todo
%{_datadir}/gpe-todo/bar-box.png
%{_datadir}/gpe-todo/dot-box.png
%{_datadir}/gpe-todo/flag-16.png
%{_datadir}/gpe-todo/notick-box.png
%{_datadir}/gpe-todo/tick-box.png
