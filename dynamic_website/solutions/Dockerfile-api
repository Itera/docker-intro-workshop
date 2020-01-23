# Build image
FROM microsoft/dotnet:2.2-sdk as build

WORKDIR /app

COPY . .

RUN dotnet publish ValuesApi.csproj -c Release -o out

# Runtime image
FROM microsoft/dotnet:2.2-aspnetcore-runtime AS runtime

WORKDIR /app

COPY --from=build /app/out .

ENTRYPOINT ["dotnet", "ValuesApi.dll"]
