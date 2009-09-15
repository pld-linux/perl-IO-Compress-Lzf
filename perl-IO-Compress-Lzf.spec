#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Compress-Lzf
Summary:	Modules to read/write lzf files/buffers
Summary(pl.UTF-8):	Moduły do odczytu/zapisu plików/buforów lzf
Name:		perl-IO-Compress-Lzf
Version:	2.021
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a705e0a225206a6241d64192b709cde4
URL:		http://search.cpan.org/dist/IO-Compress-Lzf/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Compress-LZF
BuildRequires:	perl-IO-Compress >= %{version}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Compress::Lzf and IO::Uncompress::UnLzf modules provide a Perl
interface that allows reading and writing lzf compressed data from/to
files or buffer.

Note that although this module uses Compress::LZF for compression, it
uses a different file format. The lzf file format used here is the
same as the lzf command-line utility that ships with the lzf library.

%description -l pl.UTF-8
Moduły IO::Compress::Lzf i IO::Uncompress::UnLzf udostępniają perlowy
interfejs umożliwiający odczyt i zapis danych skompresowanych
algorytmem lzf z/do plików lub buforów.

Należy zauważyć, że choć ten moduł wykorzystuje do kompresji moduł
Compress::LZF, używa innego formatu plików. Używany tutaj format
plików jest taki sam jak narzędzia lzf uruchamianego z linii poleceń,
dostarczanego wraz z biblioteką lzf.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Compress/Adapter/Lzf.pm
%{perl_vendorlib}/IO/Compress/Lzf.pm
%{perl_vendorlib}/IO/Uncompress/Adapter/Lzf.pm
%{perl_vendorlib}/IO/Uncompress/UnLzf.pm
%{_mandir}/man3/IO::*
