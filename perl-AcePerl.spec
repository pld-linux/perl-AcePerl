%include	/usr/lib/rpm/macros.perl
Summary:	AcePerl perl module
Summary(pl):	Modu³ perla AcePerl
Name:		perl-AcePerl
Version:	1.67
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Ace/AcePerl-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AcePerl provides an interface to the ACEDB object-oriented database.

%description -l pl
AcePerl umo¿liwia dostêp do obiektowej bazy danych ACEDB.

%prep
%setup -q -n AcePerl-%{version}

%build
echo "3" | perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}" \
	COMPILER="%{__cc} -DACEDB4 %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%{perl_sitearch}/Ace.pm
%{perl_sitearch}/GFF

%dir %{perl_sitearch}/Ace
%{perl_sitearch}/Ace/*.pm
%dir %{perl_sitearch}/Ace/Sequence
%{perl_sitearch}/Ace/Sequence/*.pm

%dir %{perl_sitearch}/auto/Ace
%{perl_sitearch}/auto/Ace/*.al
%{perl_sitearch}/auto/Ace/autosplit.ix
%dir %{perl_sitearch}/auto/Ace/Freesubs
%{perl_sitearch}/auto/Ace/Freesubs/Freesubs.bs
%attr(755,root,root) %{perl_sitearch}/auto/Ace/Freesubs/Freesubs.so
%{perl_sitearch}/auto/Ace/Object
%{perl_sitearch}/auto/Ace/Sequence

%{_examplesdir}/%{name}-%{version}

%{_mandir}/man3/*
