# Lab image for CVE-2026-115560 (PHP session upload progress handler mismatch).
# php:8.4.27-apache = patched for CVE-2026-109618/109619 (2026-10-21 emergency
# release) but NOT for CVE-2026-115560, which is unfixed at time of writing
# (regular release cycle per php.net 2026-10-23 advisory).
FROM php:8.4.27-apache

COPY src/ /var/www/html/

# Writable drop dir used by the PoC to prove code execution over HTTP.
RUN install -d -o www-data -g www-data /var/www/html/p
