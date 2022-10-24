JSONObject json = new JSONObject(jsonString);
JSONArray jsonArray = json.getJSONArray("key");
for (int i = 0; i < jsonArray.length(); i++) {
    JSONObject jsonObject = jsonArray.getJSONObject(i);
    String value = jsonObject.getString("key");
}