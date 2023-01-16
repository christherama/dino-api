FROM stoplight/prism:4
COPY api/docs/openapi.yaml /config/openapi.yaml
CMD ["mock", "-h", "0.0.0.0", "-d", "/config/openapi.yaml"]
