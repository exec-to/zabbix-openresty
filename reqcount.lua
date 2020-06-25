 -- reqcount.lua
 local _R = {}

 local requests = {
}

 function _R.incr(host)
     local counter = requests[host]
     if counter then
	requests[host] = counter + 1
     else
	requests[host] = 1
     end
 end

 function _R.get_printable()
     local res = ""
     for k,v in pairs(requests) do
       res = res .. k .. ":" .. v .. "\n"
     end
     return res
 end

 return _R
