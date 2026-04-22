/**
 * Convenience helper for the common authenticated-client setup.
 *
 * Shipped alongside the generated code. Users can either use this one-liner:
 *
 *     import { createClient } from "@promptcloud/scrapix";
 *     const api = createClient("YOUR_API_KEY");
 *     const { data } = await api.scrape({ url: "https://example.com" });
 *
 * …or drop down to `new Configuration(...) + new APIServicesApi(...)` when
 * they need a custom axios instance, interceptors, or extra options.
 */
import { APIServicesApi } from "./api";
import { Configuration } from "./configuration";

export const DEFAULT_HOST = "https://api-scrapix.promptcloud.com";

export function createClient(
  apiKey: string,
  basePath: string = DEFAULT_HOST,
): APIServicesApi {
  return new APIServicesApi(
    new Configuration({ apiKey, basePath }),
  );
}
