Name:     topgrade
Version:  16.2.1
Release:  latest%{?dist}
Summary:  Upgrade all the things

License:  GPL-3.0-or-later
URL:      https://github.com/topgrade-rs/topgrade
Source:   https://github.com/topgrade-rs/topgrade/archive/refs/tags/v%{version}.tar.gz

BuildRequires:   rust
BuildRequires:   cargo

%description
Topgrade is a tool that keeps your system up to date
by invoking multiple package managers.
It detects which tools you use and runs the appropriate
commands to update them.

%prep
%autosetup

%build
cargo build --release

%install
install -Dm755 target/release/topgrade %{buildroot}/usr/bin/topgrade

%files
%license LICENSE
%doc README.md
/usr/bin/topgrade

%changelog
%autochangelog
