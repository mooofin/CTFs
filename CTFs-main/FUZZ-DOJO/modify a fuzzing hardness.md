## Modify a Fuzzing Harness  minizip

This challenge demonstrates the direct relationship between a fuzzing harness and code coverage. In libFuzzer-based workflows, coverage is determined entirely by what the harness executes. If the harness does not drive execution into the target library, coverage drops to zero regardless of how long fuzzing runs.



The project was compiled using:

```bash
/challenge/build
```

This builds minizip with fuzzing support enabled and copies the fuzz drivers into a persistent directory under:

```
~/fuzz-dojo/training-modify
```

The directory contains multiple fuzz drivers, including `zip_fuzzer.c`, `unzip_fuzzer.c`, and `new_fuzzer.c`. The `new_fuzzer.c` file is a duplicate of the current top-performing fuzz driver and is intended for modification in this challenge.



The core entry point of a libFuzzer harness is the function:

```c
int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
```

In its original form, `new_fuzzer.c` contained substantial logic that exercised the minizip ZIP parsing code. A simplified excerpt of the original harness is shown below:

```c
int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    mz_zip_file *file_info = NULL;
    void *stream = NULL;
    void *handle = NULL;
    char buffer[1024];
    int32_t err = MZ_OK;

    stream = mz_stream_mem_create();
    if (!stream)
        return 1;

    mz_stream_mem_set_buffer(stream, (void *)data, (int32_t)size);

    handle = mz_zip_create();
    if (!handle)
        return 1;

    err = mz_zip_open(handle, stream, MZ_OPEN_MODE_READ);
    if (err == MZ_OK) {
        err = mz_zip_goto_first_entry(handle);
        while (err == MZ_OK) {
            err = mz_zip_entry_read(handle, buffer, sizeof(buffer));
            mz_zip_entry_close(handle);
            err = mz_zip_goto_next_entry(handle);
        }
        mz_zip_close(handle);
    }

    mz_zip_delete(&handle);
    mz_stream_mem_delete(&stream);
    return 0;
}
```

This code converts the fuzzer-provided byte buffer into an in-memory ZIP archive and drives execution through multiple parsing paths, resulting in non-zero coverage.

<img width="1880" height="762" alt="image" src="https://github.com/user-attachments/assets/dd6363b4-e22b-4c68-b480-8ec9e41ad552" />


The task was to erase the contents of the sample function and verify that coverage dropped to zero. The function body was replaced entirely with an immediate return, leaving the signature intact:

```c
int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
    return 0;
}
```

This preserves a valid fuzzing entry point while preventing any calls into the minizip library.
<img width="1891" height="790" alt="image" src="https://github.com/user-attachments/assets/bd81118e-a6ec-472a-9c66-ab0cdf977738" />



After modifying the harness, coverage analysis was run using:


```bash
/challenge/loc
```
<img width="862" height="723" alt="image" src="https://github.com/user-attachments/assets/0023b374-757c-4960-830c-1707ffb986c9" />

This command rebuilds the project, runs the fuzz driver for approximately 30 seconds, and generates a coverage report.

The resulting coverage summary for `new_fuzzer` was:

<img width="584" height="214" alt="image" src="https://github.com/user-attachments/assets/d7ea1f37-4258-4d2b-ae00-18752d43b26b" />



```
pwn.college{Eq7McVQ50FY-1PBXnRtT7m1Zrp0.dZDOyUDL0ATO0czW}
```

