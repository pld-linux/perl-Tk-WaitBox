%include	/usr/lib/rpm/macros.perl
%define	pdir	Tk
%define	pnam	WaitBox
Summary:	Tk::WaitBox - An OO Wait Dialog for Perl/Tk, of the Please Wait variety
Summary(pl):	Tk::WaitBox - obiektowe okno dialogowe oczekiwania dla Perl/Tk
Name:		perl-Tk-WaitBox
Version:	1.3
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::WaitBox is a perl5 package which implements a very flexible
WaitBox widget.

%description -l pl
Tk::WaitBox to pakiet Perla z implementacj± bardzo elastycznego
widgetu WaitBox.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Tk/WaitBox.pm
%{_mandir}/man3/*
