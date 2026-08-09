# {{SKILL_NAME}} 설치 안내

{{DESCRIPTION}}

포장한 날짜 — {{PACKED_ON}}{{AUTHOR_LINE}}

## 설치

이 zip을 풀면 `{{SKILL_NAME}}` 폴더가 나옵니다. **그 폴더를 통째로 복사**하면 끝입니다.

**복사할 폴더를 헷갈리지 마세요.** 윈도우 탐색기로 압축을 풀면 zip 이름을 딴
`{{SKILL_NAME}}-skill` 폴더가 하나 더 생깁니다. 복사할 것은 그 안의 `{{SKILL_NAME}}` 이고, 바깥
폴더가 아닙니다. 바깥 것을 복사하면 경로가 한 겹 깊어져서 스킬이 **오류 없이 그냥 안 뜹니다.**
설치가 끝나면 `SKILL.md` 가 `skills\{{SKILL_NAME}}\SKILL.md` 에 바로 있어야 맞습니다.

모든 프로젝트에서 쓰려면, Windows PowerShell에서:

```powershell
Copy-Item -Recurse .\{{SKILL_NAME}} "$HOME\.claude\skills\"
```

특정 프로젝트에서만 쓰려면, 그 프로젝트 폴더로 이동한 뒤:

```powershell
Copy-Item -Recurse .\{{SKILL_NAME}} .\.claude\skills\
```

macOS나 Linux라면 `cp -R {{SKILL_NAME}} ~/.claude/skills/` 입니다.

복사할 위치에 `skills` 폴더가 아직 없으면 먼저 만드세요.

## Claude에게 시킬 때 주의할 점

「이 폴더 읽고 스킬 설치해 줘」라고 시켜도 됩니다. 다만 한 가지만 확인하세요.

**파일 내용을 읽어서 새로 쓰는 방식이 아니라, 파일을 복사하게 해야 합니다.** `SKILL.md`를
다시 저장하면 파일 맨 앞에 BOM이라는 눈에 안 보이는 표시가 붙는 경우가 있습니다. 그러면 스킬
설정이 통째로 무시돼서, **오류 메시지 하나 없이 스킬이 그냥 안 뜹니다.** 원인을 찾기 어려운
고장이라 처음부터 복사로 하는 편이 낫습니다.

## 설치한 뒤 확인

스킬 목록은 세션이 시작될 때 읽힙니다. 설치한 그 세션에서는 안 보이는 게 정상입니다.

**새 세션을 연 다음** 스킬 목록에 `{{SKILL_NAME}}` 이 있는지 확인하세요. 새 세션에서도 안
보인다면 복사 위치가 맞는지, 폴더 안에 `SKILL.md`가 있는지 보면 됩니다.

## 필요한 것

{{REQUIREMENTS}}

## 담긴 파일

{{FILE_TABLE}}

복사가 제대로 됐는지 확인하려면, 설치한 폴더에서 아래를 돌려 위 표와 비교하세요. 값이 다르면
파일이 복사가 아니라 **다시 쓰인 것**입니다. 그 경우 zip에서 다시 복사하세요.

```powershell
$base = (Get-Location).Path.Length + 1
Get-ChildItem -Recurse -File | ForEach-Object {
  $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.Substring(0,16).ToLower()
  "{0}  {1}" -f $hash, $_.FullName.Substring($base).Replace('\','/')
}
```

## 알아둘 것

{{NOTES}}
