using System;
using System.Threading.Tasks;
using System.Net.Http;
using System.Text;
using Newtonsoft.Json;

namespace WebAPIClient {
  class Program {

    static async Task Main(string[] args) {
      await ApiCall();
    }

    private static async Task ApiCall() {

      var json = JsonConvert.SerializeObject(new {
          operatorId = "535",
          amount = "3168.4",
          useLocalAmount = false,
          customIdentifier = "This is example identifier 130",
          recipientPhone = new {
            countryCode = "GB", 
            number = "07951731337"
          },
          senderPhone = new {
            countryCode = "CA", 
            number = "11231231231"
          }
      });

      var message = new HttpRequestMessage(HttpMethod.Post, "https://topups.reloadly.com/topups"){
        Content = new StringContent(json, Encoding.UTF8, "application/json")
      };

      message.Headers.TryAddWithoutValidation("Authorization", "Bearer eyJraXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX");
      message.Headers.TryAddWithoutValidation("Accept", "application/com.reloadly.topups-v1+json");

      using
      var httpClient = new HttpClient();
      var response = await httpClient.SendAsync(message);
      var responseBody = await response.Content.ReadAsStringAsync();
      var result = JsonConvert.DeserializeObject < dynamic > (responseBody);

      Console.WriteLine(result);
    }

  }
}