using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using StackExchange.Redis;

namespace ValuesApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class RedisController : ControllerBase
    {
        private readonly IDatabase _db;
        private readonly IServer _server;

        public RedisController(IConnectionMultiplexer connectionMultiplexer)
        {
            _db = connectionMultiplexer.GetDatabase();
            _server = connectionMultiplexer.GetServer(connectionMultiplexer.GetEndPoints()[0]);
        }

        // GET api/redis
        [HttpGet]
        public async Task<ActionResult<IEnumerable<string>>> Get()
        {
            var values = new List<string>();

            foreach(var key in _server.Keys(pattern: "")) {
                var value = await _db.StringGetAsync(key);
                if (value.HasValue)
                {
                    values.Add(value);
                }
            }

            return values;
        }

        // GET api/redis/5
        [HttpGet("{id}")]
        public async Task<ActionResult<string>> Get(string id)
        {
            var redisValue = await _db.StringGetAsync(id);

            return redisValue.HasValue ? redisValue.ToString() : null;
        }

        // POST api/redis
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/redis/5
        [HttpPut("{id}")]
        public async Task Put(string id, [FromBody] string value)
        {
            await _db.StringSetAsync(id, value);
        }

        // DELETE api/redis/5
        [HttpDelete("{id}")]
        public async Task Delete(string id)
        {
            await _db.KeyDeleteAsync(id);
        }
    }
}