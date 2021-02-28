myproviders = {
    "namespaces": ["myproviders"],
    "providers": {
        "myproviders": {
            "myproviders/local/2.1.0": {
                "version": "2.1.0",
                "id": "myproviders/local/2.1.0",
                "namespace": "myproviders",
                "name": "local",
                "protocols": ["5.0"],
                "platforms": [
                    {"os": "linux", "arch": "amd64"}
                ],
                "download": {
                    "linux/amd64": {
                        "protocols": [
                            "5.0"
                        ],
                        "os": "linux",
                        "arch": "amd64",
                        "filename": "terraform-provider-local_2.1.0_linux_amd64.zip",
                        # Local source
                        "download_url": "https://localhost:8001/providers/terraform-provider-local_2.1.0_linux_amd64.zip",
                        "shasums_url": "https://releases.hashicorp.com/terraform-provider-local/2.1.0/terraform-provider-local_2.1.0_SHA256SUMS",
                        "shasums_signature_url": "https://releases.hashicorp.com/terraform-provider-local/2.1.0/terraform-provider-local_2.1.0_SHA256SUMS.sig",
                        "shasum": "0f1ec65101fa35050978d483d6e8916664b7556800348456ff3d09454ac1eae2",
                        "signing_keys": {
                            "gpg_public_keys": [
                                {
                                    "key_id": "51852D87348FFC4C",
                                    "ascii_armor": "-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v1\n\nmQENBFMORM0BCADBRyKO1MhCirazOSVwcfTr1xUxjPvfxD3hjUwHtjsOy/bT6p9f\nW2mRPfwnq2JB5As+paL3UGDsSRDnK9KAxQb0NNF4+eVhr/EJ18s3wwXXDMjpIifq\nfIm2WyH3G+aRLTLPIpscUNKDyxFOUbsmgXAmJ46Re1fn8uKxKRHbfa39aeuEYWFA\n3drdL1WoUngvED7f+RnKBK2G6ZEpO+LDovQk19xGjiMTtPJrjMjZJ3QXqPvx5wca\nKSZLr4lMTuoTI/ZXyZy5bD4tShiZz6KcyX27cD70q2iRcEZ0poLKHyEIDAi3TM5k\nSwbbWBFd5RNPOR0qzrb/0p9ksKK48IIfH2FvABEBAAG0K0hhc2hpQ29ycCBTZWN1\ncml0eSA8c2VjdXJpdHlAaGFzaGljb3JwLmNvbT6JATgEEwECACIFAlMORM0CGwMG\nCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEFGFLYc0j/xMyWIIAIPhcVqiQ59n\nJc07gjUX0SWBJAxEG1lKxfzS4Xp+57h2xxTpdotGQ1fZwsihaIqow337YHQI3q0i\nSqV534Ms+j/tU7X8sq11xFJIeEVG8PASRCwmryUwghFKPlHETQ8jJ+Y8+1asRydi\npsP3B/5Mjhqv/uOK+Vy3zAyIpyDOMtIpOVfjSpCplVRdtSTFWBu9Em7j5I2HMn1w\nsJZnJgXKpybpibGiiTtmnFLOwibmprSu04rsnP4ncdC2XRD4wIjoyA+4PKgX3sCO\nklEzKryWYBmLkJOMDdo52LttP3279s7XrkLEE7ia0fXa2c12EQ0f0DQ1tGUvyVEW\nWmJVccm5bq25AQ0EUw5EzQEIANaPUY04/g7AmYkOMjaCZ6iTp9hB5Rsj/4ee/ln9\nwArzRO9+3eejLWh53FoN1rO+su7tiXJA5YAzVy6tuolrqjM8DBztPxdLBbEi4V+j\n2tK0dATdBQBHEh3OJApO2UBtcjaZBT31zrG9K55D+CrcgIVEHAKY8Cb4kLBkb5wM\nskn+DrASKU0BNIV1qRsxfiUdQHZfSqtp004nrql1lbFMLFEuiY8FZrkkQ9qduixo\nmTT6f34/oiY+Jam3zCK7RDN/OjuWheIPGj/Qbx9JuNiwgX6yRj7OE1tjUx6d8g9y\n0H1fmLJbb3WZZbuuGFnK6qrE3bGeY8+AWaJAZ37wpWh1p0cAEQEAAYkBHwQYAQIA\nCQUCUw5EzQIbDAAKCRBRhS2HNI/8TJntCAClU7TOO/X053eKF1jqNW4A1qpxctVc\nz8eTcY8Om5O4f6a/rfxfNFKn9Qyja/OG1xWNobETy7MiMXYjaa8uUx5iFy6kMVaP\n0BXJ59NLZjMARGw6lVTYDTIvzqqqwLxgliSDfSnqUhubGwvykANPO+93BBx89MRG\nunNoYGXtPlhNFrAsB1VR8+EyKLv2HQtGCPSFBhrjuzH3gxGibNDDdFQLxxuJWepJ\nEK1UbTS4ms0NgZ2Uknqn1WRU1Ki7rE4sTy68iZtWpKQXZEJa0IGnuI2sSINGcXCJ\noEIgXTMyCILo34Fa/C6VCm2WBgz9zZO8/rHIiQm1J5zqz0DrDwKBUM9C\n=LYpS\n-----END PGP PUBLIC KEY BLOCK-----",
                                    "trust_signature": "",
                                    "source": "HashiCorp",
                                    "source_url": "https://www.hashicorp.com/security.html"
                                },
                                {
                                    "key_id": "97751AE79C450B19",
                                    "ascii_armor": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n\n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\n=X8NX\n-----END PGP PUBLIC KEY BLOCK-----",
                                    "trust_signature": "",
                                    "source": "",
                                    "source_url": None
                                }
                            ]
                        }
                    }
                }
            },
            "myproviders/local/1.4.0": {
                "version": "1.4.0",
                "id": "myproviders/local/1.4.0",
                "namespace": "myproviders",
                "name": "local",
                "protocols": ["4.0", "5.0"],
                "platforms": [
                    {"os": "linux", "arch": "amd64"}
                ],
                "download": {
                    "linux/amd64": {
                        "protocols": [
                            "4.0",
                            "5.0"
                        ],
                        "os": "linux",
                        "arch": "amd64",
                        "filename": "terraform-provider-local_1.4.0_linux_amd64.zip",
                        # Local source
                        "download_url": "https://localhost:8001/providers/terraform-provider-local_1.4.0_linux_amd64.zip",
                        "shasums_url": "https://releases.hashicorp.com/terraform-provider-local/1.4.0/terraform-provider-local_1.4.0_SHA256SUMS",
                        "shasums_signature_url": "https://releases.hashicorp.com/terraform-provider-local/1.4.0/terraform-provider-local_1.4.0_SHA256SUMS.sig",
                        "shasum": "ca9fe963f261236b3f3308f8b4979cdd95dd68281b00c1c18a6d17db07519ac8",
                        "signing_keys": {
                            "gpg_public_keys": [
                                {
                                    "key_id": "51852D87348FFC4C",
                                    "ascii_armor": "-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v1\n\nmQENBFMORM0BCADBRyKO1MhCirazOSVwcfTr1xUxjPvfxD3hjUwHtjsOy/bT6p9f\nW2mRPfwnq2JB5As+paL3UGDsSRDnK9KAxQb0NNF4+eVhr/EJ18s3wwXXDMjpIifq\nfIm2WyH3G+aRLTLPIpscUNKDyxFOUbsmgXAmJ46Re1fn8uKxKRHbfa39aeuEYWFA\n3drdL1WoUngvED7f+RnKBK2G6ZEpO+LDovQk19xGjiMTtPJrjMjZJ3QXqPvx5wca\nKSZLr4lMTuoTI/ZXyZy5bD4tShiZz6KcyX27cD70q2iRcEZ0poLKHyEIDAi3TM5k\nSwbbWBFd5RNPOR0qzrb/0p9ksKK48IIfH2FvABEBAAG0K0hhc2hpQ29ycCBTZWN1\ncml0eSA8c2VjdXJpdHlAaGFzaGljb3JwLmNvbT6JATgEEwECACIFAlMORM0CGwMG\nCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEFGFLYc0j/xMyWIIAIPhcVqiQ59n\nJc07gjUX0SWBJAxEG1lKxfzS4Xp+57h2xxTpdotGQ1fZwsihaIqow337YHQI3q0i\nSqV534Ms+j/tU7X8sq11xFJIeEVG8PASRCwmryUwghFKPlHETQ8jJ+Y8+1asRydi\npsP3B/5Mjhqv/uOK+Vy3zAyIpyDOMtIpOVfjSpCplVRdtSTFWBu9Em7j5I2HMn1w\nsJZnJgXKpybpibGiiTtmnFLOwibmprSu04rsnP4ncdC2XRD4wIjoyA+4PKgX3sCO\nklEzKryWYBmLkJOMDdo52LttP3279s7XrkLEE7ia0fXa2c12EQ0f0DQ1tGUvyVEW\nWmJVccm5bq25AQ0EUw5EzQEIANaPUY04/g7AmYkOMjaCZ6iTp9hB5Rsj/4ee/ln9\nwArzRO9+3eejLWh53FoN1rO+su7tiXJA5YAzVy6tuolrqjM8DBztPxdLBbEi4V+j\n2tK0dATdBQBHEh3OJApO2UBtcjaZBT31zrG9K55D+CrcgIVEHAKY8Cb4kLBkb5wM\nskn+DrASKU0BNIV1qRsxfiUdQHZfSqtp004nrql1lbFMLFEuiY8FZrkkQ9qduixo\nmTT6f34/oiY+Jam3zCK7RDN/OjuWheIPGj/Qbx9JuNiwgX6yRj7OE1tjUx6d8g9y\n0H1fmLJbb3WZZbuuGFnK6qrE3bGeY8+AWaJAZ37wpWh1p0cAEQEAAYkBHwQYAQIA\nCQUCUw5EzQIbDAAKCRBRhS2HNI/8TJntCAClU7TOO/X053eKF1jqNW4A1qpxctVc\nz8eTcY8Om5O4f6a/rfxfNFKn9Qyja/OG1xWNobETy7MiMXYjaa8uUx5iFy6kMVaP\n0BXJ59NLZjMARGw6lVTYDTIvzqqqwLxgliSDfSnqUhubGwvykANPO+93BBx89MRG\nunNoYGXtPlhNFrAsB1VR8+EyKLv2HQtGCPSFBhrjuzH3gxGibNDDdFQLxxuJWepJ\nEK1UbTS4ms0NgZ2Uknqn1WRU1Ki7rE4sTy68iZtWpKQXZEJa0IGnuI2sSINGcXCJ\noEIgXTMyCILo34Fa/C6VCm2WBgz9zZO8/rHIiQm1J5zqz0DrDwKBUM9C\n=LYpS\n-----END PGP PUBLIC KEY BLOCK-----",
                                    "trust_signature": "",
                                    "source": "HashiCorp",
                                    "source_url": "https://www.hashicorp.com/security.html"
                                },
                                {
                                    "key_id": "97751AE79C450B19",
                                    "ascii_armor": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n\n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\n=X8NX\n-----END PGP PUBLIC KEY BLOCK-----",
                                    "trust_signature": "",
                                    "source": "",
                                    "source_url": None
                                }
                            ]
                        }
                    }
                }
            }
        }
    }
}
