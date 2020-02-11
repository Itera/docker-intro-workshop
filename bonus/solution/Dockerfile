FROM mcr.microsoft.com/dotnet/core/sdk:2.2

COPY ValuesApi .

RUN dotnet publish ValuesApi.csproj -c Release -o out

CMD ["dotnet", "out/ValuesApi.dll"]
