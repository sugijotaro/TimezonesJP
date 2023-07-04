![](https://img.shields.io/github/license/sugijotaro/TimezonesJP)
![](https://img.shields.io/badge/PRs-welcome-orange)
![](https://img.shields.io/github/issues/sugijotaro/TimezonesJP)
![](https://img.shields.io/badge/platform-iOS-blue.svg)
# TimezonesJP

このリポジトリは、SwiftのTimeZone構造体の日本語化をサポートするためのものです。Swiftの `TimeZone.knownTimeZoneIdentifiers` メソッドで取得できる全てのタイムゾーン識別子に対応した、日本語での地域名、都市名、国名を提供します。

データは以下のURLからアクセス可能です:

https://sugijotaro.github.io/TimezonesJP/timezones.json

## 使用方法

このリポジトリで提供しているJSONデータをSwiftプロジェクトで使用する方法を示します。

まず、以下のように構造体を定義します。

```swift
struct TimeZoneSection: Codable {
    let region: String
    let region_ja: String
    let cities: [City]
    
    struct City: Codable {
        let timezone: String
        let city: String
        let country: String
        let city_ja: String
        let country_ja: String
    }
}
```
次に、JSONデータを読み込むメソッドを定義します。以下の例では、URLSessionを使用してJSONデータを非同期に読み込んでいます。
```swift
func loadTimeZones(completion: @escaping ([TimeZoneSection]?) -> Void) {
    let url = URL(string: "https://sugijotaro.github.io/TimezonesJP/timezones.json")!
    let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
        if let data = data {
            let decoder = JSONDecoder()
            if let timeZones = try? decoder.decode([TimeZoneSection].self, from: data) {
                DispatchQueue.main.async {
                    completion(timeZones)
                }
            } else {
                completion(nil)
            }
        } else {
            completion(nil)
        }
    }
    task.resume()
}
```
この関数を呼び出してデータを取得します。
```swift
loadTimeZones { timeZoneSections in
    if let timeZoneSections = timeZoneSections {
        // timeZoneSectionsを利用した処理
    } else {
        // エラーハンドリング
    }
}
```
これでSwiftのプロジェクトで利用できるようになります。

## タイムゾーン情報の追加・修正のリクエスト方法

都市や国の情報を追加または修正してほしい場合は、以下の手順でIssueを立ててください。

1. GitHubアカウントにログインします。
2. このリポジトリの「Issues」タブをクリックします。
3. 「New issue」ボタンをクリックします。
4. 「Title」欄に `Request: add [追加したい都市や国の名前]` と入力します。
5. 「Leave a comment」欄に具体的な変更内容を記載します。
6. 「Submit new issue」ボタンをクリックしてIssueを作成します。

Issueが作成されると、管理者に通知が送られ、対応が行われます。

## コントリビュート方法

直接的な貢献としてプルリクエストを送ることも大歓迎です。以下に、その手順を説明します。

1. このリポジトリをフォークします。
2. フォークしたリポジトリをローカル環境にクローンします。
3. リポジトリの `csv` ディレクトリ内の `timezones.csv` ファイルを編集します。編集する際の注意点は以下の通りです:
   -  `timezone` 列: Swiftの `TimeZone.knownTimeZoneIdentifiers` で取得できるタイムゾーン識別子を指定してください。
   -  `region`, `city`, `country` 列: 英語表記の地域名、都市名、国名を指定してください。
   -  `region_ja`, `city_ja`, `country_ja` 列: 日本語表記の地域名、都市名、国名を指定してください。
4. 編集が完了したら、変更をコミットし、そのコミットをフォークしたリポジトリにプッシュします。
5. フォークしたリポジトリから、本家のリポジトリに対してプルリクエストを作成します。プルリクエストのタイトルは `PR: add [追加したい都市や国の名前]` としてください。
6. プルリクエストの説明に、行った変更の概要を書いてください。

プルリクエストが作成されると、GitHub Actionsが動作し、編集したCSVファイルからJSONファイルが生成されます。問題がなければ、プルリクエストは管理者によりレビューされ、マージされます。

タイムゾーンの情報を共有するためにあなたの貢献をお待ちしています！

---

This repository provides Japanese representations of region, city, and country names for all timezone identifiers retrievable by Swift's `TimeZone.knownTimeZoneIdentifiers` method. It is intended to support the localization of TimeZone structs in Swift.

You can access the data from the following URL:

https://sugijotaro.github.io/TimezonesJP/timezones.json

## Usage

This section shows you how to use the JSON data provided in this repository in your Swift project.

First, define the following structs:

```swift
struct TimeZoneSection: Codable {
    let region: String
    let region_ja: String
    let cities: [City]
    
    struct City: Codable {
        let timezone: String
        let city: String
        let country: String
        let city_ja: String
        let country_ja: String
    }
}
```
Next, define a method to load the JSON data. The following example uses URLSession to load the JSON data asynchronously:
```swift
func loadTimeZones(completion: @escaping ([TimeZoneSection]?) -> Void) {
    let url = URL(string: "https://sugijotaro.github.io/TimezonesJP/timezones.json")!
    let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
        if let data = data {
            let decoder = JSONDecoder()
            if let timeZones = try? decoder.decode([TimeZoneSection].self, from: data) {
                DispatchQueue.main.async {
                    completion(timeZones)
                }
            } else {
                completion(nil)
            }
        } else {
            completion(nil)
        }
    }
    task.resume()
}
```
You can call this function to retrieve the data:
```swift
loadTimeZones { timeZoneSections in
    if let timeZoneSections = timeZoneSections {
        // Use timeZoneSections here
    } else {
        // Error handling
    }
}
```
With these steps, you can use the JSON data in your Swift project.

## Requesting Additions or Corrections to Timezone Information

If you want to add or correct information about a city or country, please raise an issue following the steps below.

1. Log in to your GitHub account.
2. Click on the 'Issues' tab of this repository.
3. Click on the 'New issue' button.
4. Enter `Request: add [name of the city or country you want to add]` in the 'Title' field.
5. Describe the specific changes in the 'Leave a comment' field.
6. Click on the 'Submit new issue' button to create the issue.

When an issue is created, a notification is sent to the administrator for action.

## How to Contribute

You are welcome to send a pull request as a direct contribution. Below are the steps to do so.

1. Fork this repository.
2. Clone the forked repository to your local environment.
3. Edit the `timezones.csv` file in the `csv` directory of the repository. When editing, note the following:
   - `timezone` column: Specify a timezone identifier that can be obtained with Swift's `TimeZone.knownTimeZoneIdentifiers`.
   - `region`, `city`, `country` columns: Specify the English names of the region, city, and country.
   - `region_ja`, `city_ja`, `country_ja` columns: Specify the Japanese names of the region, city, and country.
4. After editing, commit the changes and push the commit to the forked repository.
5. Create a pull request from the forked repository to the original repository. Please title the pull request as `PR: add [name of the city or country you want to add]`.
6. In the description of the pull request, write a summary of the changes you made.

When a pull request is created, GitHub Actions will work to generate a JSON file from the edited CSV file. If there are no problems, the pull request will be reviewed and merged by the administrator.

We look forward to your contributions to share timezone information!
